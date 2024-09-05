### Flask Todo App with Login and CRUD Operations

This is a simple todo app for anyone who wants to learn flask and its functionalities. We will be covering following topics in this project.

Based on the difficulty level I am diving into multiple parts

todoapp_CRUD - Basic Flask CRUD application with Flask-RESTful and Flask-SQLAlchemy.

1. Flask RESTful for the API endpoints.
2. Endpoints for serving the UI functionality.
3. Flask-sqlalchemy for the database.


todoapp_LOGIN - Basic Flask application with Flask-Login for user management and login functionality.

4. Flask-Login for the UI endpoints.
5. Register new user and login functionality.
5. JWT login for the API endpoints.
6. Flask-SQLAlchemy for the database.
7. Flask-Limiter for the rate limiting for around 60 requests per hour.


#### Setting up the project

1. Clone the repository
```
git clone https://github.com/yourusername/todoapp_LOGIN.git

2. Install the dependencies
```
pip install -r requirements.txt
```

Setup the database 

```
cd todoapp_CRUD or cd todoapp_LOGIN
python -m app.init_db.py
```
This will create a database file app/app.db in the app directory.

3. Run the application
```
python run.py
```
