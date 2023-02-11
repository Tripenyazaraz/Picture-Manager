from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "tag" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "type" VARCHAR(64) NOT NULL
);
COMMENT ON COLUMN "tag"."type" IS 'general: general\nauthor: author\ncharacter: character\nfandom: fandom\nmeta: meta';
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(32) NOT NULL,
    "password" VARCHAR(64) NOT NULL,
    "email" VARCHAR(254) NOT NULL
);
CREATE TABLE IF NOT EXISTS "album" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(254) NOT NULL,
    "created_by_id" INT REFERENCES "user" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "media" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "filename" VARCHAR(254) NOT NULL,
    "filepath" VARCHAR(2032) NOT NULL,
    "uploaded_by_id" INT REFERENCES "user" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "album_media" (
    "album_id" INT NOT NULL REFERENCES "album" ("id") ON DELETE CASCADE,
    "media_id" INT NOT NULL REFERENCES "media" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "media_tag" (
    "media_id" INT NOT NULL REFERENCES "media" ("id") ON DELETE CASCADE,
    "tag_id" INT NOT NULL REFERENCES "tag" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
