from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):

    __tablename__ = "city"
    name = db.Column(db.String(50), primary_key=True)
    country_name = db.Column(db.String(50), db.ForeignKey('country.name'))

    def __repr__(self) -> str:
        return f"City(name={self.name}, country_name='{self.country_name}')"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import country_controller

        return {
            "id": self.name,
            "country_name": country_controller.find_by_id(self.country_name)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:

        obj = City(
            name=dto_dict.get("name"),
            country_name=dto_dict.get("country_name")
        )
        return obj
