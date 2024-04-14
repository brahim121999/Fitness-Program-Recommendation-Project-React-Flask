

fitness recommendation api  [Flask](http://flask.pocoo.org) & [SQLAlchemy](http://www.sqlalchemy.org), and connecting the both using [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org) library.



## Getting started
* At first you'll need to get the source code of the project. Do this by cloning
```

```

* Create a virtual environment for this project and install dependencies
```
$ virtualenv .venv
```

* Activate the virtual environment
```
$ source .venv/bin/activate
```

* Install the dependencies
```
$ pip install -r requirements.txt
```

* Create a environment file and configure it
```
$ touch .env
```

#### Sample .env File
```
SECRET_KEY="w&8s%5^5vuhy2-gvkyi=gg4e*tso*51mb$l!=%o(@$a2tmq6o+Flask-SQLAlchemy-RESTful-CRUD"
DEBUG=TRUE
SQLALCHEMY_DATABASE_URI="mysql://YOUR_DB_USER_NAME:YOUR_DB_PASS@localhost:3306/YOUR_DB_NAME"
SQLALCHEMY_TRACK_MODIFICATIONS=FALSE
```

* Update `SQLALCHEMY_DATABASE_URI` at the `.env` file according to your MySQL database information


## Running the App

#### 1) With Database Migration

```
$ export FLASK_APP=app.py
$ flask db init
```

* Create a migration file for all tables
```
$ flask db migrate -m tables
```

* Upgrade the database with migration file
```
$ flask db upgrade
```

* Run the app
```
$ flask run
```

And finally, the application will run on the following URL: http://127.0.0.1:5000


#### 2) Without Migration

* Simply run the following command, it will create database tables and run the project on the following URL: http://0.0.0.0:8087
* And the DEBUG mode will be ON

```
$ python app.py
```

If you want to change the PORT go to the [app.py](https://github.com/fatematzuhora/Flask-SQLAlchemy-RESTful-CRUD/blob/master/app.py) file and edit on the following line of code.
```
app.run(host='0.0.0.0', port=8087, debug=True)
```


## API Documentation

#### 1. Create user

**Request**
```
POST /user
```


**Request Body**
```
{
    "email": "john@example.com",
        "id":1 ,
        "name": "John Doe",
        "password": "password123"
}
```

**Response**
```
{
    "data": {
        "email": "john@example.com",
        "id": 1,
        "name": "John Doe",
        "password": "password123"
    },
     "message": "New User Created!",
    "status": 201
}
```

#### 2. user List

**Request**
```
GET /user
```

**Response**
```
{
    "data": [
        {
            "email": "john@example.com",
            "id": 1,
            "name": "John Doe",
            "password": "password123"
        },
        {
            "email": "jane@example.com",
            "id": 2,
            "name": "Jane Smith",
            "password": "password456"
        },
        {
            "email": "user@gmail.com",
            "id": 4,
            "name": "John Doe",
            "password": "password123"
        }
    ],
    "message": "All Users!",
    "status": 200
}
```

#### 3. user Detail

**Request**
```
GET /user/:id
```

**Response**
```
{
    "data": {
        "email": "john@example.com",
        "id": 1,
        "name": "John Doe",
        "password": "password123"
    },
    "message": "User Info!",
    "status": 200
}
```

#### 4. Update user

**Request**
```
PATCH /user/:id
```



#### 5. Delete user

**Request**
```
DELETE /user/:id
```

**Response**
```
{
    "message": "User Deleted!",
    "status": 200
}
```
