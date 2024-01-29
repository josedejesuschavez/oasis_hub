from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from iam.infrastructure.ui.router import iam_router


app = FastAPI()

# Clave secreta utilizada para firmar los tokens
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


# Función para generar un token JWT
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


# Función para decodificar y verificar un token JWT
def decode_jwt_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


# Función para obtener el usuario actual basado en el token JWT
def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = {"sub": username}
    except JWTError:
        raise credentials_exception
    return token_data


# Ruta protegida que requiere autenticación
@app.get("/protected")
async def protected_route(current_user=Depends(get_current_user)):
    return {"message": "This is a protected route", "username": current_user["sub"]}


# Ruta para obtener un token de acceso
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = {"username": form_data.username, "password": form_data.password}
    # Realizar la autenticación (simulada en este ejemplo)
    if user_dict["username"] == "user" and user_dict["password"] == "password":
        token_data = {"sub": form_data.username}
        access_token = create_jwt_token(token_data)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(iam_router.router, prefix="/iam", tags=["iam"])


@app.post("/clicked")
async def read_users():
    button = "<button class='btn btn-primary'>Login</button>"
    return HTMLResponse(content=button, status_code=200)
