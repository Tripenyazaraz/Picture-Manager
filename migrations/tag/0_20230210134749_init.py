from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "tagmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "type" VARCHAR(64) NOT NULL
);
CREATE TABLE IF NOT EXISTS "usermodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(32) NOT NULL,
    "password" VARCHAR(64) NOT NULL,
    "email" VARCHAR(254) NOT NULL
);
CREATE TABLE IF NOT EXISTS "albummodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(254) NOT NULL,
    "created_by_id" INT REFERENCES "usermodel" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "mediamodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "filename" VARCHAR(254) NOT NULL,
    "filepath" VARCHAR(2032) NOT NULL,
    "uploaded_by_id" INT REFERENCES "usermodel" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "albummodel_mediamodel" (
    "albummodel_id" INT NOT NULL REFERENCES "albummodel" ("id") ON DELETE CASCADE,
    "mediamodel_id" INT NOT NULL REFERENCES "mediamodel" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "mediamodel_tagmodel" (
    "mediamodel_id" INT NOT NULL REFERENCES "mediamodel" ("id") ON DELETE CASCADE,
    "tagmodel_id" INT NOT NULL REFERENCES "tagmodel" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
