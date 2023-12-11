from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class StreetAdress(db.Model, IDto):
    __tablename__ = "street_adress"

    name = db.Column(db.String(50), primary_key=True)
    city_name = db.Column(db.String(50), db.ForeignKey('city.name'))
    city_country_name = db.Column(db.String(50), db.ForeignKey('city.country_name'))
    airport_id = db.Column(db.Integer, db.ForeignKey('airport.id'))

    def __repr__(self) -> str:
        return f"StreetAdress(name={self.name}, city_name='{self.city_name}', " \
               f"city_country_name='{self.city_country_name}', airport_id='{self.airport_id}')"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import city_controller
        from laba4.app.my_project.auth.controller import airport_controller

        return {
            "name": self.name,
            "city_name": city_controller.find_by_id(self.city_name),
            "city_country_name": city_controller.find_by_id(self.city_country_name),
            "airport_id": airport_controller.find_by_id(self.airport_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StreetAdress:
        obj = StreetAdress(
            name=dto_dict.get("name"),
            city_name=dto_dict.get("city_name"),
            city_country_name=dto_dict.get("city_country_name"),
            airport_id=dto_dict.get("airport_id"),
        )
        return obj
