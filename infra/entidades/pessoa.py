from sqlalchemy import Column, Integer, String
from infra.config.base import Base
from sqlalchemy.orm import relationship


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(30))
    senha = Column(String(8), nullable=False)
    endereco = relationship("Endereco", backref='endereco', lazy='subquery')

    def __repr__(self):
        return f' Pessoa {self.nome}'