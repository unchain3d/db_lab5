from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class Client(db.Model, IDto):

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    birthday = db.Column(db.DATE, nullable=False)
    phone = db.Column(db.String(13), nullable=True)

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.surname}', '{self.name}', " \
               f"'{self.birthday}', '{self.phone}')"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "surname": self.surname,
            "name": self.name,
            "birthday": self.birthday,
            "phone": self.phone
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:

        obj = Client(
            surname=dto_dict.get("surname"),
            name=dto_dict.get("name"),
            birthday=dto_dict.get("birthday"),
            phone=dto_dict.get("phone")
        )
        return obj
