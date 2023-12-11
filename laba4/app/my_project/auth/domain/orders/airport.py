from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Airport(db.Model, IDto):

    __tablename__ = "airport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plane = db.Column(db.Integer)
    name = db.Column(db.String(45))


    def __repr__(self) -> str:
        return f"Airport(id={self.id}, plane={self.plane}, " \
               f"name={self.name})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "plane": self.plane,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Airport:

        obj = Airport(
            id=dto_dict.get("id"),
            plane=dto_dict.get("plane"),
            name=dto_dict.get("name")
        )
        return obj
