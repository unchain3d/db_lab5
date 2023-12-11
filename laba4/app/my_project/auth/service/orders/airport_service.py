from laba4.app.my_project.auth.dao import airport_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class AirportService(GeneralService):
    _dao = airport_dao
