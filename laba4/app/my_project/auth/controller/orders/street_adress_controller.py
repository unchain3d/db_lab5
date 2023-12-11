from laba4.app.my_project.auth.service import street_adress_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class StreetAdressController(GeneralController):

    _service = street_adress_service
