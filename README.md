# fastapi-keycloak-template

An template for fast api in connection with keycloak

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
