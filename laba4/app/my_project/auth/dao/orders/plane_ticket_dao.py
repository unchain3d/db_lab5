from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.plane_ticket import PlaneTicket


class PlaneTicketDAO(GeneralDAO):
    _domain_type = PlaneTicket
