from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class PlaneTicket(db.Model, IDto):

    __tablename__ = "plane_ticket"
    seat = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=True)

    def __repr__(self) -> str:
        return f"PlaneTicket(seat={self.seat},price={self.price}, client_id={self.client_id}, " \
               f"flight_id={self.flight_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import client_controller
        from laba4.app.my_project.auth.controller import plane_ticket_controller
        return {
            "seat": self.seat,
            "price": self.price,
            "client_id": client_controller.find_by_id(self.client_id),
            "flight_id": plane_ticket_controller.find_by_id(self.flight_id)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PlaneTicket:

        obj = PlaneTicket(
            seat=dto_dict.get("seat"),
            price=dto_dict.get("price"),
            client_id=dto_dict.get("client_id"),
            flight_id=dto_dict.get("flight_id")
        )
        return obj
