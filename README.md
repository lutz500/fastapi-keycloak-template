# FastAPI Keycloak Template

This repository contains a template for integrating **FastAPI** with **Keycloak** for user management. It also considers an additional database using **PostgreSQL** for storing user and application data.

## Features

- **FastAPI**: Modern web framework for building APIs with Python 3.7+ based on standard Python-type hints.
- **Keycloak**: Open-source Identity and Access Management for modern applications and services.
- **PostgreSQL**: Relational database system for storing data.
- **Docker Compose**: To manage multi-container Docker applications (Keycloak, PostgreSQL, and FastAPI).


# Usage
To use this Code apply the following steps:

1. Create a Venv:
```
python -m venv <myenvpath>
```

2. Install requirements:
```
pip install -r src/requirements/requirements.txt
```

3. Create a `.env`-file:
```
DATABASE_URL = postgresql+asyncpg://username:password@host:port
KEYCLOAK_ADMIN = <admin-username>
KEYCLOAK_ADMIN_PASSWORD = <admin-password>
KEYCLOAK_REALM=<realm-name>
KEYCLOAK_CLIENT_ID=<client-name>
KEYCLOAK_CLIENT_SECRET=<client-secrect>
ALGORITHM = RS256
MODE=<DEV or PROD>
```

4. Start all docker container:
```
docker compose up
```
