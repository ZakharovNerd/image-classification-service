import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf

from src.containers.containers import AppContainer
from src.routes.routers import router as app_router
from src.routes import predict as predict_routes


def app() -> FastAPI:
    container = AppContainer()
    cfg = OmegaConf.load('config/config.yml')
    container.config.from_dict(cfg)
    container.wire([predict_routes])

    app = FastAPI()
    app.include_router(app_router, prefix='/classifier', tags=['poster'])
    return app


if __name__ == '__main__':
    app = app()
    uvicorn.run(app, port=2444, host='0.0.0.0')
