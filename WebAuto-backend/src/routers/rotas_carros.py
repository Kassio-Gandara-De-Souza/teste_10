from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Carro, CarroSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_carro \
    import RepositorioCarro

router = APIRouter()


@router.post('/carros',
             status_code=status.HTTP_201_CREATED,
             response_model=CarroSimples)
def cadastrar_carro(
        carro: Carro,
        session: Session = Depends(get_db)):
    carro_criado = RepositorioCarro(session).criar(carro)
    return carro_criado


@router.get('/carros', response_model=List[Carro])
def listar_carros(session: Session = Depends(get_db)):
    carros = RepositorioCarro(session).listar()
    return carros


@router.get('/carros/{id}')
def exibir_carro(id: int, session: Session = Depends(get_db)):
    carro_localizado = RepositorioCarro(session).buscarPorId(id)
    if not carro_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um carro com o id = {id}')
    return carro_localizado


@router.put('/carros/{id}', response_model=CarroSimples)
def atualizar_carro(
        id: int,
        carro: Carro,
        session: Session = Depends(get_db)):
    RepositorioCarro(session).editar(id, carro)
    carro.id = id
    return carro


@router.delete('/carros/{id}')
def remover_carro(id: int, session: Session = Depends(get_db)):
    RepositorioCarro(session).remover(id)
    return {"mensagem":"Carro removido com sucesso!"}
