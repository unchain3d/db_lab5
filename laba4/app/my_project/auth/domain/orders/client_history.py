from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class ClientHistory(db.Model, IDto):

    __tablename__ = "client_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    info = db.Column(db.String(45), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True)


    def __repr__(self) -> str:
        return f"ClientHistory({self.id}, '{self.info}', '{self.client_id}')"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import client_controller
        return {
            "id": self.id,
            "info": self.info,
            "client_id": client_controller.find_by_id(self.client_id)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ClientHistory:

        obj = ClientHistory(
            info=dto_dict.get("info"),
            client_id=dto_dict.get("client_id")
        )
        return obj
