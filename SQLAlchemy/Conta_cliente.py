from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Column

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(9), nullable=False, unique=True)
    endereco = Column(String(100), nullable=False)

    conta = relationship(
        "Conta", 
        back_populates="cliente", 
        cascade="all, delete-orphan")

    def __repr__(self):
        return f"Cliente( id = {self.id}, nome = {self.nome}, cpf = {self.cpf}, endereco = {self.endereco})"



class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, unique=True)
    tipo = Column(String(30), nullable=True)
    agencia = Column(String(10), nullable=True)
    num = Column(Integer, nullable= True)
    id_cliente = Column(Integer, ForeignKey('Clientes.id'), unique=True)

    cliente = relationship(
        "Cliente", 
        back_populates="conta")

    def __repr__(self):
        return f"Conta (id = {self.id}, tipo = {self.tipo}, agencia = {self.agencia}, num = {self.num}, id_cliente = {self.id_cliente})"
