from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class AirlineCompany(db.Model, IDto):
    __tablename__ = "airline_company"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    plane = db.Column(db.Integer)


    def __repr__(self) -> str:
        return f"AirlineCompany(id={self.id},name={self.name}, plane={self.plane})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "plane": self.plane
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AirlineCompany:
        obj = AirlineCompany(
            id= dto_dict.get("id"),
            name=dto_dict.get("name"),
            plane=dto_dict.get("plane"),
        )
        return obj
