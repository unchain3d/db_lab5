from laba4.app.my_project.auth.dao import country_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class CountryService(GeneralService):
    _dao = country_dao