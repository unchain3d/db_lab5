from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .orders.airline_company_route import airline_company_bp
    from .orders.city_route import city_bp
    from .orders.airport_route import airport_bp
    from .orders.client_route import client_bp
    from laba4.app.my_project.auth.route.orders.client_history_route import client_history_bp
    from laba4.app.my_project.auth.route.orders.country_route import country_bp
    from laba4.app.my_project.auth.route.orders.flight_route import flight_bp
    from laba4.app.my_project.auth.route.orders.luggage_constraints_route import luggage_constraints_bp
    from .orders.street_adress_route import street_adress_bp
    from laba4.app.my_project.auth.route.orders.plane_ticket_route import plane_ticket_bp
    app.register_blueprint(airline_company_bp)
    app.register_blueprint(airport_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(client_history_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(flight_bp)
    app.register_blueprint(luggage_constraints_bp)
    app.register_blueprint(plane_ticket_bp)
    app.register_blueprint(street_adress_bp)