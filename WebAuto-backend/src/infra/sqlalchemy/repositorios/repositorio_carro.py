from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
# from sqlalchemy.sql.expression import select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioCarro():

    def __init__(self, db: Session):
        self.session = db

    def criar(self, carro: schemas.Carro):
        db_carro = models.Carro(modelo=carro.modelo,
                                    marca=carro.marca,
                                    ano=carro.ano,
                                    preco=carro.preco,
                                    quilometragem=carro.quilometragem,
                                    local=carro.local,
                                    cor=carro.cor,
                                    usuario_id=carro.usuario_id)
        self.session.add(db_carro)
        self.session.commit()
        self.session.refresh(db_carro)
        return db_carro

    def listar(self):
        carros = self.session.query(models.Carro).all()
        return carros

    def buscarPorId(self, id: int):
        consulta = select(models.Carro).where(models.Carro.id == id)
        carro = self.session.execute(consulta).first()
        return carro

    def editar(self, id: int, carro: schemas.Carro):
        update_stmt = update(models.Carro).where(
            models.Carro.id == id).values(modelo=carro.modelo,
                                            marca=carro.marca,
                                            ano=carro.ano,
                                            preco=carro.preco,
                                            quilometragem=carro.quilometragem,
                                            local=carro.local,
                                            cor=carro.cor,
                                            )
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, id: int):
        delete_stmt = delete(models.Carro).where(
            models.Carro.id == id
        )

        self.session.execute(delete_stmt)
        self.session.commit()
