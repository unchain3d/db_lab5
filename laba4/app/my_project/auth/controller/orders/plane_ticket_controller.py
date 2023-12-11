from laba4.app.my_project.auth.service import plane_ticket_service
from laba4.app.my_project.auth.controller.general_controller import GeneralController


class PlaneTicketController(GeneralController):

    _service = plane_ticket_service