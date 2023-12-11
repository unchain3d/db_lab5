from laba4.app.my_project.auth.service import flight_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class FlightController(GeneralController):

    _service = flight_service