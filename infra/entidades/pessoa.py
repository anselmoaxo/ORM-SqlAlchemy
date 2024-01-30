from sqlalchemy import Column, Integer, String
from infra.config.base import Base


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(30))

    def __repr__(self):
        return f' Pessoa {self.nome}'