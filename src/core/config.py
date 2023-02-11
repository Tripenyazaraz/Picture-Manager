from starlette.config import Config

config = Config(".env")

SERVER_PORT = config("SERVER_PORT", cast=int, default=8002)
TIMEZONE = config("TIMEZONE", cast=str, default="Asia/Almaty")

PG_DB_HOST = config("PG_DB_HOST", cast=str, default="127.0.0.1")
PG_DB_PORT = config("PG_DB_PORT", cast=int, default=5432)
PG_DB_NAME = config("PG_DB_NAME", cast=str, default="nsfw")
PG_DB_USERNAME = config("PG_DB_USERNAME", cast=str, default="postgres")
PG_DB_PASSWORD = config("PG_DB_PASSWORD", cast=str, default="admin")

TORTOISE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": PG_DB_NAME,
                "host": PG_DB_HOST,
                "password": PG_DB_PASSWORD,
                "port": PG_DB_PORT,
                "user": PG_DB_USERNAME,
            }
        }
    },
    "apps": {
        "album": {
            "models": ["src.apps.album.models", "aerich.models"],
            "default_connection": "default",
        },
        "media": {
            "models": ["src.apps.media.models", "aerich.models"],
            "default_connection": "default",
        },
        "tag": {
            "models": ["src.apps.tag.models", "aerich.models"],
            "default_connection": "default",
        },
        "user": {
            "models": ["src.apps.user.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
