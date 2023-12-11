from laba4.app.my_project.auth.dao import client_history_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class ClientHistoryService(GeneralService):
    _dao = client_history_dao