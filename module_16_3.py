from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr

app = FastAPI()

# Словарь для хранения пользователей
users = {
	'1': 'Имя: Example, возраст: 18'
}


class User(BaseModel):
	username: constr(min_length=1)  # минимальная длина имени пользователя - 1 символ
	age: int  # возраст пользователя


@app.get('/')
async def read_root():
	return {"message": "Welcome to the User Management API"}


@app.get('/users')
async def get_users():
	return users


@app.post('/user/{username}/{age}', response_model=str)
async def create_user(username: str, age: int):
	if age < 0:
		raise HTTPException(status_code=400, detail="Age must be non-negative")

	user_id = str(max(map(int, users.keys()), default=0) + 1)
	users[user_id] = f"Имя: {username}, возраст: {age}"
	return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}', response_model=str)
async def update_user(user_id: str, username: str, age: int):
	if user_id not in users:
		raise HTTPException(status_code=404, detail="User not found")

	if age < 0:
		raise HTTPException(status_code=400, detail="Age must be non-negative")

	users[user_id] = f"Имя: {username}, возраст: {age}"
	return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}', response_model=str)
async def delete_user(user_id: str):
	if user_id not in users:
		raise HTTPException(status_code=404, detail="User not found")

	del users[user_id]
	return f"User {user_id} has been deleted"