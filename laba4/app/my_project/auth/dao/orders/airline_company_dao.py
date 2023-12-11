from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain import AirlineCompany


class AirlineCompanyDAO(GeneralDAO):

    _domain_type = AirlineCompany
