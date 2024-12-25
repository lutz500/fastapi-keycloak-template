# fastapi-keycloak-template

This repository contains a template for a FastAPI with Keyloak as user management.
An additional database using postgres is considered.

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
