from typing import List
from fastapi import APIRouter, Depends

from sql import SQLiteDB
from models import Friend, Friends, NewFriendCreated



router = APIRouter(
	prefix = "/api/friends"
)



@router.post("/create", response_model = NewFriendCreated, tags = ["FRIENDS"])
async def create_friend(
	friend: Friend,
	db=Depends(SQLiteDB)
	):
	
	name, age , pet = friend.name, friend.age, friend.pet

	cmd="insert into friends values(?,?,?)"
	values=(name, age, pet) 

	# hier kommt nun zum tragen, dass instanzen 
	# von SQLiteDB aufrufbar sind. in unserem 
	# konkreten falle bringt das wenig 
	# erleichterung aber man kann es mal gesehen haben.^^
	db(cmd, values)
	
	return {
		"status": "success",
		"data": [{
			"name": name,
			"age": age, 
			"pet": pet
		}]
	}


@router.get("/", response_model=Friends, tags=["FRIENDS"])
async def get_all_friends(db=Depends(SQLiteDB)):
	friends = []
	for row in db("select * from friends"):
		name, age, pet = row
		friends.append({
			"name": name,
			"age": age,
			"pet": bool(pet) # pet wird als 0 oder 1 ausgeliefert.
		})

	return {
		"status": "success",
		"data": friends
	}

	 
	