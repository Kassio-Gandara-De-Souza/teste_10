from pydantic import BaseModel
from typing import Optional, List


class CarroSimples(BaseModel):
    id: Optional[int] = None
    modelo: str
    preco: float

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    carros: List[CarroSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    senha: str
    telefone: str


class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str


class Carro(BaseModel):
    id: Optional[int] = None
    modelo: str
    marca: str
    ano: int
    preco: float
    quilometragem: float
    local: str
    cor: str
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'

    usuario_id: Optional[int]
    carro_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    carro: Optional[CarroSimples]

    class Config:
        orm_mode = True
