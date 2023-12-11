from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.client import Client


class ClientDAO(GeneralDAO):

    _domain_type = Client