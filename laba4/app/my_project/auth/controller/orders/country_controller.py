from laba4.app.my_project.auth.service import country_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class CountryController(GeneralController):

    _service = country_service