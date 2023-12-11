from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.country import Country


class CountryDAO(GeneralDAO):

    _domain_type = Country