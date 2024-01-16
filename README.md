# Flask TodoList App

This is a simple TodoList application built using Flask, SQLAlchemy, and PostgreSQL.


## Run Locally

Clone the project

```bash
  git clone https://github.com/anupamhaldkar/UdacityTodoApp
```

Go to the project directory

```bash
  cd UdacityTodoApp
```

Create a virtual environment and install dependencies:

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
  pip install -r requirements.txt
```

Set up the PostgreSQL database

- Create a database named `todolist_db`.

Configure the Flask app

- Open app.py and update the database URI with your PostgreSQL credentials:
```bash
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/todolist_db'
```
Initialize the database
```bash
    python app.py
```

Start the server

```bash
    flask run

```

Access the TodoList app in your web browser at `http://localhost:5000/`.

## Features

- View all tasks on the main page.
- Add new tasks using the "Add Task" button.
- Update tasks by clicking on the task and modifying the title.
- Delete tasks by clicking the "Delete" button.
## Authors

- [@anupamhaldkar](https://www.github.com/anupamhaldkar)

