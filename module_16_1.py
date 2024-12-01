from fastapi import FastAPI

app = FastAPI()  # Создаем экземпляр приложения FastAPI

@app.get("/")  # Маршрут для главной страницы
async def read_main():
    return {"message": "Главная страница"}

@app.get("/user/admin")  # Маршрут для страницы администратора
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")  # Маршрут для страниц пользователей с параметром в пути
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")  # Маршрут для страниц пользователей с параметрами в адресной строке
async def read_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}