from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.street_adress import StreetAdress


class StreetAdressDAO(GeneralDAO):
    _domain_type = StreetAdress