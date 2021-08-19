CREATE DATABASE "$POSTGRES_NAME" ENCODING 'utf-8';
CREATE USER "$POSTGRES_USER" WITH password '$POSTGRES_PASSWORD';
GRANT ALL privileges ON DATABASE "$POSTGRES_NAME" TO "$POSTGRES_USER";
ALTER DATABASE "$POSTGRES_NAME" OWNER TO "$POSTGRES_USER";
ALTER USER "$POSTGRES_USER" CREATEDB;
