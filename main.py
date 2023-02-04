import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.core.config import PG_DB_USERNAME, PG_DB_PASSWORD, PG_DB_HOST, PG_DB_PORT, PG_DB_NAME, SERVER_PORT

app = FastAPI(
    title="NutSafelyForWeal",
    debug=True
)


@app.on_event("startup")
async def init_db():
    register_tortoise(
        app=app,
        db_url=f"asyncpg://{PG_DB_USERNAME}:{PG_DB_PASSWORD}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}",
        modules={"models": ["src.apps.album.models", "src.apps.media.models", "src.apps.tag.models", "src.apps.user.models"]},
        generate_schemas=True,
        add_exception_handlers=True
    )
    Tortoise.init_models(["src.apps.album.models", "src.apps.media.models", "src.apps.tag.models", "src.apps.user.models"], "models")

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=SERVER_PORT, host="0.0.0.0", reload=True, workers=26)
