import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.entities.user import User

prefix = "http://localhost:8000/users"

def list_users():
    response = requests.get(prefix)
    assert response.status_code == 200

def testUnit():
    assert isinstance(User(1,'RAfa', 'sadlasd', 'adsads'), User) == True
    assert isinstance(User.hash_password('OPA'), str) == True
    assert User.hash_password('OPA') == '581f127fb797adbd97f21d2121f8319e1143c34e4faa611881df5b7045432a9e'
    assert isinstance(User.create_by_obj({'id': 1, 'nickname': 'Rafa', 'password': 'asdkasda', 'password_salt': 'asdads'}), User) == True