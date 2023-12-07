import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.entities.history import History

prefix = "http://localhost:8000/histories"

def list_histories():
    response = requests.get(prefix)
    assert response.status_code == 200

def testUnit():
    assert isinstance(History(1,'Teste','asdkasda','humor','asdads',1), History) == True
    assert isinstance(History.create_by_obj({'id': 1, 'title': 'Teste', 'summary': 'asdkasda', 'category': 'humor', 'content': 'asdads', 'user_id': 1}), History) == True