from typing import List
from pydantic import (
	BaseModel, 
	ValidationError, 
	validator
)



class Friend(BaseModel):
	name: str
	age: int
	pet: bool


class NewFriendCreated(BaseModel):
	status: str
	data: List[Friend]


class Friends(BaseModel):
	status: str
	data: List[Friend]