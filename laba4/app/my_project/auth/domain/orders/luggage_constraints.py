from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db
from laba4.app.my_project.auth.domain.i_dto import IDto


class LuggageConstraints(db.Model,IDto):

    __tablename__ = "luggage_constraints"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    max_weight = db.Column(db.Integer, nullable=False)
    max_height = db.Column(db.Integer, nullable=False)
    max_length = db.Column(db.Integer, nullable=False)
    max_width = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"LuggageConstraints(id={self.id}, max_weight='{self.max_weight}', max_height='{self.max_height}', " \
               f"nax_length='{self.max_length}', max_width='{self.max_width})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "max_height": self.max_height,
            "max_length": self.max_length,
            "max_width": self.max_width

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> LuggageConstraints:

        obj = LuggageConstraints(
            max_weight=dto_dict.get("max_weight"),
            max_height=dto_dict.get("max_height"),
            max_length=dto_dict.get("max_length"),
            max_width=dto_dict.get("max_width")

        )
        return obj
