import logging
import sys


from fastapi import FastAPI

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

