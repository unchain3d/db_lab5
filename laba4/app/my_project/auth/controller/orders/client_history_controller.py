from laba4.app.my_project.auth.service import client_history_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class ClientHistoryController(GeneralController):

    _service = client_history_service