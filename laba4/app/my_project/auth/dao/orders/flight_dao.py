from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.flight import Flight


class FlightDAO(GeneralDAO):
    _domain_type = Flight
