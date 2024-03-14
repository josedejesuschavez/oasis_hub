from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse(
        request=request, name="iam/login.html", context={}
    )
