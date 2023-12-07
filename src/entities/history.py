from src.daos.history_dao import history_dao

class History():
    def __init__(self, id, title, summary, category, content, user_id):
        self.id = id
        self.title = title 
        self.summary = summary 
        self.category = category 
        self.content = content 
        self.user_id = user_id

    @staticmethod
    def create_by_obj(history: dict) :
        return History(history.get("id"), history.get("title"), history.get("summary"), history.get("category"), history.get("content"), history.get("user_id"))

    @staticmethod
    def create_by_obj_arr(histories):
        history_instances = []
        for history in histories:
            history_instances.append(History.create_by_obj(history))
        return history_instances

    @staticmethod
    def get_by_id(id): 
        history = history_dao.get_by_id(id)
        return History.create_by_obj(history)
    
    @staticmethod
    def list_by_user_id(id):
        histories = history_dao.list_by_user_id(id)
        return History.create_by_obj_arr(histories)
    
    @staticmethod
    def list_histories():
        return History.create_by_obj_arr(history_dao.list())
    
    @staticmethod
    def create(title, summary, category, content, user_id):
        history_id = history_dao.create(title,   summary, category, content, user_id)
        return History.get_by_id(history_id)
    
    def delete(self):
        history_dao.delete(self.id)

    def save(self):
        history_dao.update(self.id, self.title, self.summary, self.category, self.content, self.user_id)
    