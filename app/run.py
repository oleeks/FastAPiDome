import uvicorn

import logging

from app.api import create_app

# logging.getLogger('gino.engine._SAEngine').setLevel(logging.ERROR)

if __name__ == '__main__':
    run_app = create_app()
    uvicorn.run(run_app, host="127.0.0.1", port=8000)
