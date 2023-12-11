from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.luggage_constraints import LuggageConstraints


class LuggageConstraintsDAO(GeneralDAO):
    _domain_type = LuggageConstraints