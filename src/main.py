from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from iam.infrastructure.ui.router import iam_router
from ui_builder.infrastructure.ui.router import ui_builder_router


app = FastAPI()


@app.post("/login")
async def login_post(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = {"username": form_data.username, "password": form_data.password}
    if (
        user_dict["username"] == "user@correo.com"
        and user_dict["password"] == "123qweQWE"
    ):
        return {"access_token": "sdfsdfsdf", "token_type": "bearer"}

    alert = """<div role="alert" class="alert alert-error" x-data="{ show: true }" x-show="show">
                <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                <span>Error! Invalid credentials</span>
                <button @click="show = false" class="close-btn">&times;</button>
            </div>"""

    return HTMLResponse(content=alert, status_code=200)


templates = Jinja2Templates(directory="templates")

app.include_router(iam_router.router, prefix="/iam", tags=["iam"])
app.include_router(ui_builder_router.router, prefix="/ui_builder", tags=["ui_builder"])


@app.post("/clicked")
async def read_users():
    button = "<button class='btn btn-primary'>Login</button>"
    return HTMLResponse(content=button, status_code=200)
