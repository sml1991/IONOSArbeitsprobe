import os
import friends_router 

from fastapi import FastAPI
from sql import SQLiteDB



def make_app() -> FastAPI:
	
	app = FastAPI(
		title = "IONOSArbeitsprobe",
		debug = os.environ.get("DEBUG"))
	
	cmd = \
	"create table if not exists friends "\
	"(name str, age int, pet bool)"

	db=SQLiteDB()
	db(cmd)

	app.include_router(friends_router.router)
	
	return app



app = make_app()

