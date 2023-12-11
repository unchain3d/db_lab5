from laba4.app.my_project.auth.dao import plane_ticket_dao
from laba4.app.my_project.auth.service.general_service import GeneralService


class PlaneTicketService(GeneralService):
    _dao = plane_ticket_dao