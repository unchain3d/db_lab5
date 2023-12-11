from laba4.app.my_project.auth.dao import airline_company_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AirlineCompanyService(GeneralService):
    _dao = airline_company_dao
