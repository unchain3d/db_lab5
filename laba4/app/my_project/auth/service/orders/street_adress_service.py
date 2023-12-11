from laba4.app.my_project.auth.dao import street_adress_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class StreetAdressService(GeneralService):
    _dao = street_adress_dao