from .orders.airline_company_dao import AirlineCompanyDAO
from .orders.airport_dao import AirportDAO
from .orders.city_dao import CityDAO
from .orders.client_dao import ClientDAO
from .orders.client_history_dao import ClientHistoryDAO
from .orders.country_dao import CountryDAO
from .orders.flight_dao import FlightDAO
from .orders.luggage_constraints_dao import LuggageConstraintsDAO
from .orders.plane_ticket_dao import PlaneTicketDAO
from .orders.street_adress_dao import StreetAdressDAO

airline_company_dao = AirlineCompanyDAO()
airport_dao = AirportDAO()
city_dao = CityDAO()
client_dao = ClientDAO()
client_history_dao = ClientHistoryDAO()
country_dao = CountryDAO()
flight_dao = FlightDAO()
luggage_constraints_dao = LuggageConstraintsDAO()
plane_ticket_dao = PlaneTicketDAO()
street_adress_dao = StreetAdressDAO()
