from __future__ import annotations
from typing import Dict, Any

from laba4.app.my_project import db


class Country(db.Model):

    __tablename__ = "country"

    name = db.Column(db.String(50), primary_key=True)

    def __repr__(self) -> str:
        return f"Countries(name={self.name})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "name": self.name,
        }

#DB object (DBO) into DTO (JSON)

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Country:

        obj = Country(
            name=dto_dict.get("name")
        )
        return obj

# Процес НАВПАКИ