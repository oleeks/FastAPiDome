import uvicorn
from fastapi import FastAPI

from fastapi_dome.app.api import user
from fastapi_dome.app.ext import db

def get_app():
    app = FastAPI(title="GINO FastAPI Demo")
    db.init_app(app)
    user.init_app(app)
    return app


if __name__ == '__main__':
    run_app = get_app()
    uvicorn.run(run_app, host="127.0.0.1", port=8000)
