from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Пустой список для хранения пользователей
users = []


# Класс User, наследованный от BaseModel
class User(BaseModel):
	id: int  # номер пользователя
	username: str  # имя пользователя
	age: int  # возраст пользователя


@app.get('/')
async def read_root():
	return {"message": "Welcome to the User Management API"}


@app.get('/users', response_model=list[User])
async def get_users():
	return users


@app.post('/user/{username}/{age}', response_model=User)
async def create_user(username: str, age: int):
	if age < 0:
		raise HTTPException(status_code=400, detail="Age must be non-negative")

	user_id = (max(user.id for user in users) + 1) if users else 1
	new_user = User(id=user_id, username=username, age=age)
	users.append(new_user)
	return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, username: str, age: int):
	user = next((user for user in users if user.id == user_id), None)

	if user is None:
		raise HTTPException(status_code=404, detail="User was not found")

	if age < 0:
		raise HTTPException(status_code=400, detail="Age must be non-negative")

	user.username = username
	user.age = age
	return user


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
	user = next((user for user in users if user.id == user_id), None)

	if user is None:
		raise HTTPException(status_code=404, detail="User was not found")

	users.remove(user)
	return user
