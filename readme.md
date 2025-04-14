# Run Instructions #

This project has 3 parts:

- Backend: Python Flask
- Frontend: ReactJS
- Database: MySQL

each of these is in a docker container, and running docker compose up will start running them.

- `docker compose up`: start running the docker containers
- `docker compose up --build`: Build and run
- `docker compose up -d`: Run in detached mode (background)

After running docker compose up, wait a couple of minutes since the database takes a little while to come up.

If the database is new, it will not contain any tables. These need to be populated using flask migrate.
which needs to run outside the container.

If running outside docker:

for backend end:

1. cd app
2. activate venv: `source venv/bin/activate`
3. install dependencies in venv: `pip install -r requirements.txt`
4. flask run

for front end:

1. cd frontend
2. npm install
3. npm start

for database: It has to be run from docker, use `docker compose up db` to run just the database

## Flask Migrate Instructions

1. activate the virtual environment

    `source venv/bin/activate`

2. install all dependencies into the virtualenv

    `pip install -r requirements.txt`

3. migrate the database.

    `flask db upgrade`

    If the migrations/versions are not present then run, they need to be initialized before the upgrade command:

    `flask db init`  
