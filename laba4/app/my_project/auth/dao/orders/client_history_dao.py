from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.client_history import ClientHistory


class ClientHistoryDAO(GeneralDAO):

    _domain_type = ClientHistory
