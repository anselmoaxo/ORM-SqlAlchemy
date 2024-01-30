from infra.config.connection import DBConnectionHandler
from infra.entidades.endereco import Endereco
from infra.entidades.pessoa import Pessoa


class EnderecoRepositorio:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Endereco).join(Pessoa, Endereco.pessoa == Pessoa.id).with_entities(
                Endereco.logradouro,
                Endereco.cidade,
                Pessoa.nome).all()
            return data