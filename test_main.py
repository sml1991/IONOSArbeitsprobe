import sys
import os
import json
from fastapi.testclient import TestClient
from main import app 


client = TestClient(app)


######################################

def test_read_friends():
    resp = client.get("/api/friends")
    assert resp.status_code == 200

#######################################


def test_create_friend():

    uri="/api/friends/create"

    homer = {"name": "Homer", "age": 46, "pet": True}
    marge = {"name": "Marge", "age": "34", "pet": True}
    bart = {"name": "Bart", "age": "twelve", "pet": True}

    resp_homer = client.post(uri, json=homer)
    resp_marge = client.post(uri, json=marge)
    resp_bart  = client.post(uri, json=bart)

    assert resp_homer.status_code == 200
    assert resp_marge.status_code == 200 # der string 'age' wird automatisch gewandelt
    assert resp_bart.status_code != 200 # das sollte allerdings nicht funktionieren

    # der status '200' garantiert natürlich noch nicht die korrektheit der
    # tatsächlich zurückgelieferten danten. müsste man gesondert testen.