## Presentation

* This project is realised by Ibrahim Braham & Badr-Eddine Jouad & Mamadou Lamine Dikhaby as part of Back-end and Front-end 
* web development cours taken in Paris Dauphine University

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

* Don't forget to add the API keys that we will send you via email into the openai_service.py and the pincone_service.py files
* Due to github rules we can't upload the .env file

And finally, the application will run on the following URL: http://127.0.0.1:5000
