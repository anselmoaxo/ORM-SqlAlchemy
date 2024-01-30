from sqlalchemy import Column, Integer, String, ForeignKey
from infra.config.base import Base
from sqlalchemy.orm import relationship


class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    logradouro = Column(String(50))
    cidade = Column(String(30))
    pessoa = Column(Integer, ForeignKey("pessoa.id"))
    

    def __repr__(self):
        return f' Endereco {self.logradouro} - {self.cidade}, / Pessoa= {self.pessoa}'