from flask import Flask , abort, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://anupam:password@localhost:5432/todoapp'
db = SQLAlchemy(app)

migrate = Migrate(app,db)

#create user in psql by these commands
# CREATE USER/ROLE ANUPAM SUPERUSER WITH PASSWORD "";
#\du display user
#\h query to help
#ALTER ROLE anupam WITH ENCRYPTED PASSWORD "";
#\c - <username> change 
#\c <dbname> change
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(),nullable=False)
    completed = db.Column(db.Boolean(),default=False)
    list_id = db.Column(db.Integer,db.ForeignKey('todolists.id'),nullable=False)
    
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

#db.create_all()
class TodoList(db.Model):
    __tablename__ = 'todolists'
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),nullable=False)
    todos = db.relationship('Todo',backref='list',lazy=True)

@app.route('/TodoApp/create', methods=['POST'])
def create_todo():
    error = False
    body={}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error=True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    if not error:
        return jsonify(body)

@app.route('/todoApp/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        print('completed', completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))   

@app.route('/todoApp/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })

@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html',
    lists=TodoList.query.all(),
    active_list=TodoList.query.get(list_id),
    todos=Todo.query.filter_by(list_id=list_id).order_by('id')
    .all()
    )

@app.route('/')
def index():
    return redirect(url_for('get_list_todos',list_id=1))
