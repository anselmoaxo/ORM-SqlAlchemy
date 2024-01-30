from infra.config.connection import DBConnectionHandler
from infra.entidades.pessoa import Pessoa


class PessoaRepositorio:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Pessoa).all()
            return data
        
    def inserir(self, nome, email):
        with DBConnectionHandler() as db:
            inserir_pessoa = Pessoa(nome=nome, email=email)
            db.session.add(inserir_pessoa)
            db.session.commit()
            
    def deletar(self, nome):
        with DBConnectionHandler() as db:
            db.session.query(Pessoa).filter(Pessoa.nome == nome).delete()
            db.session.commit()
            
    def update(self, nome, email):
        with DBConnectionHandler() as db:
            db.session.query(Pessoa).filter(Pessoa.nome == nome).update({'email':email})
            db.session.commit()