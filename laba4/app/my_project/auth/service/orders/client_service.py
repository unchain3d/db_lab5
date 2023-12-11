from laba4.app.my_project.auth.dao import client_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    _dao = client_dao
