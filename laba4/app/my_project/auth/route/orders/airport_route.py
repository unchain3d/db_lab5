from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import airport_controller
from laba4.app.my_project.auth.domain.orders.airport import Airport

airport_bp = Blueprint('airport', __name__, url_prefix='/airport')


@airport_bp.get('')
def get_all_airports() -> Response:

    return make_response(jsonify(airport_controller.find_all()), HTTPStatus.OK)


@airport_bp.post('')
def create_airport() -> Response:
    content = request.get_json()
    airport = Airport.create_from_dto(content)
    airport_controller.create(airport)
    return make_response(jsonify(airport.put_into_dto()), HTTPStatus.CREATED)


@airport_bp.get('/<int:airport_id>')
def get_airport(airport_id: int) -> Response:

    return make_response(jsonify(airport_controller.find_by_id(airport_id)), HTTPStatus.OK)


@airport_bp.put('/<int:airport_id>')
def update_airport(airport_id: int) -> Response:

    content = request.get_json()
    airport = Airport.create_from_dto(content)
    airport_controller.update(airport_id, airport)
    return make_response("Airport updated", HTTPStatus.OK)


@airport_bp.patch('/<int:airport_id>')
def patch_airport(airport_id: int) -> Response:

    content = request.get_json()
    airport_controller.patch(airport_id, content)
    return make_response("Airport updated", HTTPStatus.OK)


@airport_bp.delete('/<int:airport_id>')
def delete_airport(airport_id: int) -> Response:

    airport_controller.delete(airport_id)
    return make_response("Airport deleted", HTTPStatus.OK)