from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from iam.infrastructure.ui.router import iam_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(iam_router.router, prefix="/iam", tags=["iam"])


@app.post("/clicked")
async def read_users():
    button = "<button class='btn btn-primary'>Login</button>"
    return HTMLResponse(content=button, status_code=200)
