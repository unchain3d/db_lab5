from laba4.app.my_project.auth.service import airline_company_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class AirlineCompanyController(GeneralController):

    _service = airline_company_service
