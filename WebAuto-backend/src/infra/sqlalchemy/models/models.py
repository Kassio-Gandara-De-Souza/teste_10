from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    carros = relationship('Carro', back_populates='usuario')
    pedidos = relationship('Pedido', back_populates='usuario')


class Carro(Base):
    __tablename__ = 'carro'

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    marca = Column(String)
    ano = Column(String)
    preco = Column(Float)
    quilometragem = Column(Float)
    local = Column(String)
    cor = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))

    usuario = relationship('Usuario', back_populates='carros')


class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    local_entrega = Column(String)
    tipo_entrega = Column(String)
    observacao = Column(String)

    usuario_id = Column(Integer, ForeignKey(
        'usuario.id', name='fk_pedido_usuario'))
    carro_id = Column(Integer, ForeignKey(
        'carro.id', name='fk_pedido_carro'))

    usuario = relationship('Usuario', back_populates='pedidos')
    carro = relationship('Carro')
