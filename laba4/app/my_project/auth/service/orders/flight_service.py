from laba4.app.my_project.auth.dao import flight_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class FlightService(GeneralService):
    _dao = flight_dao