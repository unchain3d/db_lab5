from laba4.app.my_project.auth.service import luggage_constraints_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class LuggageConstraintsController(GeneralController):

    _service = luggage_constraints_service