from laba4.app.my_project.auth.dao import city_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class CityService(GeneralService):
    _dao = city_dao