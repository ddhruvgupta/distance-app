# Run Instructions #

## Running on a new machine ##

Make sure there are no previous containers with the names:

1. `flask` - this is the name used by the backend container.
2. `frontend` - this is the name used by the frontend container.
3. `db` - this is the name used by the database container.

Changing the names is complicated, some hardcoded strings might need to be changed and is considered future work.

`docker compose -f target-docker-compose.yaml up -d`

the -d tag creates a daemon. If you want to see the logs, run it without -d.

- [backend](!localhost:5000)
- [Swagger](!localhost:5000/docs)
- [frontend](!localhost:3000)

The Flask Application needs the db to be running. Sometimes with docker compose, the db might not be ready for the flask app and the container will fault.
After waiting for a few seconds for the db to come up, you can run `docker compose up flask -d`.

## Running Locally with git clone ##

This project has 3 parts:

- Backend: Python Flask
- Frontend: ReactJS
- Database: MySQL

each of these is in a docker container, and running docker compose up will start running them.

- `docker compose up --build`: Build and run
- `docker compose up`: start running the docker containers
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

for database:

It has to be run from docker, use `docker compose up db` to run just the database

or setup a local mysql instace running on port 3306.

## Flask Migrate Instructions (Manual)

*If connecting a new database, the migration should execute automatically.*

1. activate the virtual environment

    `source venv/bin/activate`

2. install all dependencies into the virtualenv

    `pip install -r requirements.txt`

3. migrate the database.

    `flask db upgrade`

    If the migrations/versions are not present then run, they need to be initialized before the upgrade command:

    `flask db init`  

## Publishing the docker images: Makefile ##

The makefile has commands to make a new build. The Username is currently hardcoded.

`make build`

`make push`

## Future Work ##

1. CORS config for backend
2. API route versioning.
3. Create Base Controller and use that in other controllers.
4. Clean up / refactoring of front end:
    - Use Hooks
    - Single Responsibility Principle
    -
