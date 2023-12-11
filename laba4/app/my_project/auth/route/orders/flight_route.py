from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import flight_controller
from laba4.app.my_project.auth.domain.orders.flight import Flight

flight_bp = Blueprint('flight', __name__, url_prefix='/flight')


@flight_bp.get('')
def get_all_flights() -> Response:
    return make_response(jsonify(flight_controller.find_all()), HTTPStatus.OK)


@flight_bp.post('')
def create_flight() -> Response:
    content = request.get_json()
    item = Flight.create_from_dto(content)
    flight_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@flight_bp.get('/<int:item_id>')
def get_flight(item_id: int) -> Response:
    return make_response(jsonify(flight_controller.find_by_id(item_id)), HTTPStatus.OK)


@flight_bp.put('/<int:item_id>')
def update_flight(item_id: int) -> Response:
    content = request.get_json()
    item = Flight.create_from_dto(content)
    flight_controller.update(item_id, item)
    return make_response("flight updated", HTTPStatus.OK)


@flight_bp.patch('/<int:item_id>')
def patch_flight(item_id: int) -> Response:
    content = request.get_json()
    flight_controller.patch(item_id, content)
    return make_response("flight updated", HTTPStatus.OK)


@flight_bp.delete('/<int:item_id>')
def delete_flight(item_id: int) -> Response:
    flight_controller.delete(item_id)
    return make_response("flight deleted", HTTPStatus.OK)