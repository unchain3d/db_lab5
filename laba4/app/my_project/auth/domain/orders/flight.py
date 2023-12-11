from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Flight(db.Model, IDto):

    __tablename__ = "flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    duration = db.Column(db.Integer, nullable=True)
    starting_point = db.Column(db.Integer, db.ForeignKey('airport.id'), nullable=True)
    destination_point = db.Column(db.Integer, db.ForeignKey('airport.id'), nullable=True)
    luggage_constraints_id = db.Column(db.Integer, db.ForeignKey('luggage_constraints.id'), nullable=True)
    next_connected_flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=True)

    def __repr__(self) -> str:
        return f"Flight(id={self.id}, duration={self.duration}, starting_point={self.starting_point}" \
               f"destination_point={self.destination_point}, luggage_constraints_id={self.luggage_constraints_id}" \
               f"next_connected_flight_id = {self.next_connected_flight_id})"

    def put_into_dto(self) -> Dict[str, Any]:

        from laba4.app.my_project.auth.controller import airport_controller
        from laba4.app.my_project.auth.controller import flight_controller

        return {
            "id": self.id,
            "duration": self.duration,
            "starting_point": airport_controller.find_by_id(self.starting_point),
            "destination_point": airport_controller.find_by_id(self.destination_point),
            "luggage_constraints_id": self.luggage_constraints_id,
            "next_connected_flight_id": flight_controller.find_by_id(self.next_connected_flight_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Flight:

        obj = Flight(
            id=dto_dict.get("id"),
            duration=dto_dict.get("duration"),
            starting_point=dto_dict.get("starting_point"),
            destination_point=dto_dict.get("destination_point"),
            luggage_constraints=dto_dict.get("luggage_constraints"),
            next_connected_flight=dto_dict.get("next_connected_flight"),

        )
        return obj
