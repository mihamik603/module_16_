from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse
from typing import Annotated

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Главная страница"

# Страница администратора
@app.get("/user/admin", response_class=HTMLResponse)
async def read_admin():
    return "Вы вошли как администратор"

# Страница пользователя по user_id с валидацией
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID")]
):
    return f"Вы вошли как пользователь № {user_id}"

# Страница пользователя с параметрами в пути и валидацией
@app.get("/user/{username}/{age}", response_class=HTMLResponse)
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
