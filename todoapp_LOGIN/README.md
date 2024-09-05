#### Continuing with our todo app, we will be adding login functionality to the app. We will be using Flask-Login for endpoints that serve the UI and JWT for API endpoints that are protected. 

#### Flask-login for the UI endpoints.

/login - By default if the user is already logged in then it will redirect to the index page else will serve the login page.
/register - For registering new users. 
/logout - By default if the user is already logged in then it will redirect to the login page else will serve the logout page.

@login_required - This is a decorator that is used to protect the routes that are only accessible to the logged in users which is used above the routes that are protected.

sqlalchemy models.py - Contains the models for the database and tables will be created by initiating init_db.py file in following way
```
cd todoapp_LOGIN
python -m app. init_db.py
```
This will create app/app.db file which will be your primary database file with sample user already added.

Schema for the users table.

```
id - primary key
username - string, unique, indexed, nullable
email - string, unique, indexed, nullable
password_hash - string, nullable
role - string, nullable

```

#### JWT for the API endpoints.

/api/login - POST - For logging in the users and getting the access token.
/api/tasks - GET, POST - For getting all the tasks and adding a new task.
/api/tasks/<int:task_id> - GET, PUT, DELETE - For getting, updating and deleting the task by id.

You can use the endpoints in following way.

To get the access token for the user, you can use the following command.
```
curl -X POST http://localhost:5000/api/login -H "Content-Type: application/json" -d '{"username": "sampleuser", "password": "password"}' |  jq -r .access_token
```

You shoud get the acess token in response like this 
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNTI5MjIxMiwianRpIjoiY2MyYmQ4MzEtZjkxNy00ZWYzLWExY2MtMWI2YjJhOTEwODU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzI1MjkyMjEyLCJjc3JmIjoiOWZmODA5OWYtZGQ0Zi00YTc1LTkwODYtNGJhNjM0OGNkMjM1IiwiZXhwIjoxNzI1MjkzMTEyfQ.jjV1L6rrhCdK4Rzrm3vEWcONvIvMkhoKNyfVrAA5bcw
```

Use that access token in following command to access the tasks.

```
curl -X GET http://localhost:5000/api/tasks -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNTI5MjIxMiwianRpIjoiY2MyYmQ4MzEtZjkxNy00ZWYzLWExY2MtMWI2YjJhOTEwODU4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzI1MjkyMjEyLCJjc3JmIjoiOWZmODA5OWYtZGQ0Zi00YTc1LTkwODYtNGJhNjM0OGNkMjM1IiwiZXhwIjoxNzI1MjkzMTEyfQ.jjV1L6rrhCdK4Rzrm3vEWcONvIvMkhoKNyfVrAA5bcw"
```
