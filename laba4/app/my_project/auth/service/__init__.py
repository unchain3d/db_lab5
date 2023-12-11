from .orders.airline_company_service import AirlineCompanyService
from .orders.airport_service import AirportService
from .orders.city_service import CityService
from .orders.client_service import ClientService
from .orders.client_history_service import ClientHistoryService

from .orders.country_service import CountryService
from .orders.flight_service import FlightService
from .orders.luggage_constraints_service import LuggageConstraintsService
from .orders.plane_ticket_service import PlaneTicketService
from .orders.street_adress_service import StreetAdressService

airline_company_service = AirlineCompanyService()
airport_service = AirportService()
city_service = CityService()
client_service = ClientService()
client_history_service = ClientHistoryService()

country_service = CountryService()
flight_service = FlightService()
luggage_constraints_service = LuggageConstraintsService()
plane_ticket_service = PlaneTicketService()
street_adress_service = StreetAdressService()
