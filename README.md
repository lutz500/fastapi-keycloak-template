# fastapi-keycloak-template

This repository contains a template for a FastAPI with Keyloak as user management.
An additional database using postgres is considered.

Create an `.env` file with following content:

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
