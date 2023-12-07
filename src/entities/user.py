from src.daos.user_dao import user_dao
from src.entities.history import History
import random
import hashlib
import jwt

class User():
    def __init__(self, id, nickname, password, password_salt):
        self.id = id
        self.nickname = nickname 
        self.password = password 
        self.password_salt = password_salt

    @staticmethod
    def create_by_obj(user: dict):
        return User(user.get("id"), user.get("nickname"), user.get("password"), user.get("password_salt"))

    @staticmethod
    def create_by_obj_arr(users):
        user_instances = []
        for user in users:
            user_instances.append(User.create_by_obj(user))
        return user_instances

    @staticmethod
    def get_by_id(id): 
        user = user_dao.get_by_id(id)
        return User.create_by_obj(user)
    
    @staticmethod
    def hash_password(password: str):
        hash_obj = hashlib.sha256()
        hash_obj.update(password.encode('utf-8'))
        return hash_obj.hexdigest()

    @staticmethod
    def create(nickname, password):
        password_salt = random.randint(1000, 9999)
        result = user_dao.create(nickname, User.hash_password(f"{password}{password_salt}"), password_salt)
        return result
    
    @staticmethod
    def login(nickname, password):
        user = User.create_by_obj(user_dao.get_by_nickname(nickname))
        return user.try_login(password)
    
    @staticmethod
    def list_users():
        users_info = user_dao.list()
        print("=====================================", users_info)
        return User.create_by_obj_arr(users_info)
    
    def make_token(self):
        payload = {
            'id': self.id
        }
        return jwt.encode(payload, 'teste', algorithm="HS256")
    
    @staticmethod
    def get_user_by_token(token: str):
        try:
            payload = jwt.decode(token, 'teste', algorithms=["HS256"])
            print(payload.get('id'))
            return User.get_by_id(payload.get('id'))
        except jwt.ExpiredSignatureError:
            print("Token expirado")
            return None
        except jwt.InvalidTokenError:
            print("Token inválido")
            return None
    
    def update_password(self, password):
        password_salt = random.randint(1000, 9999)
        self.password_salt = password_salt
        self.password = User.hash_password(f"{password}{password_salt}")
    
    def list_histories(self):
        return History.list_by_user_id(self.id)
    
    def try_login(self, password):
        hashed_password = User.hash_password(f"{password}{self.password_salt}")

        if(hashed_password == self.password):
            return self
        else:
            return False
        
    def delete(self):
        user_dao.delete(self.id)
    
    def save(self):
        user_dao.update(self.id, self.nickname, self.password, self.password_salt)