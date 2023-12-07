from src.daos.history_dao import history_dao
from src.config.openai_config import openai_connection

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

    def add_part_and_merge_with_gpt(self, part: str):
        newContent = openai_connection.request_prompt(f"Tenho uma história e preciso adicionar um trecho nela na parte onde mais se encaixar. Pode fazer as modficiações necessárias na história como um todo. PRECISO QUE SUA RESPOSTA SEJA APENAS A HISTÓRIA CORRIGIDA COM A PARTE ADICIONAL ADAPTADA, SEM TÍTULO, DESCRIÇÃO, CATEGORIA OU OUTROS CAMPOS. NÃO INSIRA ASPAS SIMPLES OU DUPLAS NO TEXTO. Informações de base:\n Título: '{self.title}';\n descricao='{self.summary}';\n categoria:'{self.category}';\n história base: '{self.content}'\n; trecho para ser adicionado: '{part}'.\n LEMBRE-SE QUERO APENAS O RESULTADO FINAL DA HISTÓRIA ADAPTADA COM O CONTEÚDO INSERIDO. NÃO MANDE AS INFORMAÇÔES DE BASE NOVAMENTE")
        self.content = newContent
        self.save()

    def save(self):
        history_dao.update(self.id, self.title, self.summary, self.category, self.content, self.user_id)
    