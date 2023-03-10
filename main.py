import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.core.config import SERVER_PORT, TORTOISE_CONFIG
from src.apps.album.routes import router as album_router
from src.apps.media.routes import router as media_router
from src.apps.tag.routes import router as tag_router
from src.apps.user.routes import router as user_router

app = FastAPI(
    title="NutSafelyForWeal",
    debug=True
)

app.include_router(album_router)
app.include_router(media_router)
app.include_router(tag_router)
app.include_router(user_router)


@app.on_event("startup")
async def init_db():
    # await Tortoise.init(
    #     config={
    #         "connections": {
    #             "default": {
    #                 "engine": "tortoise.backends.asyncpg",
    #                 "credentials": {
    #                     "database": PG_DB_NAME,
    #                     "host": PG_DB_HOST,
    #                     "password": PG_DB_PASSWORD,
    #                     "port": PG_DB_PORT,
    #                     "user": PG_DB_USERNAME,
    #                 }
    #             }
    #         },
    #         "apps": {
    #             "album": {
    #                 "models": ["src.apps.album.models"],
    #                 "default_connection": "default",
    #             },
    #             "media": {
    #                 "models": ["src.apps.media.models"],
    #                 "default_connection": "default",
    #             },
    #             "tag": {
    #                 "models": ["src.apps.tag.models"],
    #                 "default_connection": "default",
    #             },
    #             "user": {
    #                 "models": ["src.apps.user.models"],
    #                 "default_connection": "default",
    #             },
    #         },
    #     }
    # )
    register_tortoise(
        app=app,
        config=TORTOISE_CONFIG
    )
    # db_url=f"asyncpg://{PG_DB_USERNAME}:{PG_DB_PASSWORD}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}",
    # modules={
    #     "album": ["src.apps.album.models"],
    #     "media": ["src.apps.media.models"],
    #     "tag": ["src.apps.tag.models"],
    #     "user": ["src.apps.user.models"],
    # },
    # generate_schemas=True,
    # add_exception_handlers=True

    # Tortoise.init_models(["src.apps.user.models"], "user")
    # Tortoise.init_models(["src.apps.tag.models"], "tag")
    # Tortoise.init_models(["src.apps.media.models"], "media")
    # Tortoise.init_models(["src.apps.album.models"], "album")

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=SERVER_PORT, host="0.0.0.0", reload=True, workers=26)
