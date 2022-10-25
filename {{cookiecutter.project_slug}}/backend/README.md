# Backend Application

Contains the API portion of the system.
Uses Fastapi to serve CRUD routes.
Database is postgres docker container, modelled and connected with sqlalchemy backend via sqlmodel, using alembic to control models in database

## Dependencies
- python 3.10>

## Installation
setup the environment
```
poetry shell
poetry install
```
setup pre-commit for development hooks
```
pre-commit install
```
## Running
from app directory (with requirements.txt and poetry.lock)
```
uvicorn app.main:app
```