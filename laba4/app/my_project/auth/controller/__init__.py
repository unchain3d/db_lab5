from .orders.airline_company_controller import AirlineCompanyController
from .orders.city_controller import CityController
from .orders.country_controller import CountryController
from .orders.street_adress_controller import StreetAdressController

from .orders.airport_controller import AirportController
from .orders.luggage_constraints_controller import LuggageConstraintsController
from .orders.client_controller import ClientController
from .orders.plane_ticket_controller import PlaneTicketController
from .orders.flight_controller import FlightController
from .orders.client_history_controller import ClientHistoryController

airline_company_controller = AirlineCompanyController()
airport_controller = AirportController()
city_controller = CityController()
client_controller = ClientController()
client_history_controller = ClientHistoryController()
country_controller = CountryController()
flight_controller = FlightController()
luggage_constraints_controller = LuggageConstraintsController()
plane_ticket_controller = PlaneTicketController()
street_adress_controller = StreetAdressController()
