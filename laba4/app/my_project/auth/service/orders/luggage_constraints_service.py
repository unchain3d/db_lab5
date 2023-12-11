from laba4.app.my_project.auth.dao import luggage_constraints_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class LuggageConstraintsService(GeneralService):
    _dao = luggage_constraints_dao