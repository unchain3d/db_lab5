from laba4.app.my_project.auth.service import airport_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AirportController(GeneralController):

    _service = airport_service