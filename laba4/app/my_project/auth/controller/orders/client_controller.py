from laba4.app.my_project.auth.service import client_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):

    _service = client_service