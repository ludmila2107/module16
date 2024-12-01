from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()  # Создаем экземпляр приложения FastAPI

@app.get("/")  # Маршрут для главной страницы
async def read_main():
    return {"message": "Главная страница"}

@app.get("/user/admin")  # Маршрут для страницы администратора
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")  # Маршрут для страниц пользователей с параметром в пути с валидацией
async def read_user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID")]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")  # Обновленный маршрут для страниц пользователей с параметрами в пути
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}