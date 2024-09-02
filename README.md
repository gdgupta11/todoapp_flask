### I have been teaching couple of students devops and python. This is the repo for the students to follow along for creating the todo app. Slowly we will be adding more features to the app.

* In this the first app is a simple todo app where we will learn how to create a todo app with flask, sqlalchemy, blueprints and CRUD operations. 

* We will be using Flask Framework for this app.
* How large flask application should be structured.
* How to use blueprints in flask for each different API modules. Here we have created 2 blueprints for the application. One for the API and another for the UI routes that will be used to render the html pages.
* How config management is done in flask.
* How to initialize the logging in app context and use it across the application.

### UI Documentation

Here the UI routes are created using flask. We have created a UI for the app.

/ -> Home page
/create -> Create a new task

/update/<int:id> -> Update a task

/delete/<int:id> -> Delete a task

/get/<int:id> -> Get a task by id



### API documentation 

#### Get all tasks
Endpoint: GET /tasks
Description: Retrieves a list of all tasks.
Example:

```
GET /tasks
Response:
[
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description 1",
        "completed": false
    },

]
```

If you want to call it via curl then you can use the following command.
```
curl http://127.0.0.1:5000/api/tasks
```

#### Get a task by id
Endpoint: GET /tasks/<int:task_id>
Description: Retrieves a task by its ID.
Example:
```
GET /api/tasks/1
Response:
{
    "id": 1,
    "title": "Task 1",
    "description": "Description 1",
    "completed": false
}
```

#### Create a new task
Endpoint: POST /tasks
Description: Creates a new task.
Example:
```
POST /api/tasks
Request Body:
{
    "title": "New Task",
    "description": "Description of the new task"
}
Response:
{
    "id": 2,
    "title": "New Task",
    "description": "Description of the new task",
    "completed": false
}
```

#### Update a task
Endpoint: PUT /api/tasks/<int:task_id>  
Description: Updates a task by its ID.
Example:
```
PUT /tasks/1
Request Body:
{
    "title": "Updated Task",
    "description": "Updated description of the task"
}   
Response:
{
    "id": 1,
    "title": "Updated Task",
    "description": "Updated description of the task",
    "completed": false
}
```

#### Delete a task
Endpoint: DELETE /api/tasks/<int:task_id>
Description: Deletes a task by its ID.
Example:
DELETE /api/tasks/1
Response:
{
    "message": "Task with ID 1 has been deleted."
}   
```