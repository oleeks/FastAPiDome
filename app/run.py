import uvicorn
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
os.sys.path.append(BASE_DIR)

from app.api import create_app

# logging.getLogger('gino.engine._SAEngine').setLevel(logging.ERROR)

if __name__ == '__main__':
    run_app = create_app()
    uvicorn.run(run_app, host="127.0.0.1", port=8000)
