from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import luggage_constraints_controller
from laba4.app.my_project.auth.domain.orders.luggage_constraints import LuggageConstraints

luggage_constraints_bp = Blueprint('luggage_constraints', __name__, url_prefix='/luggage_constraints')


@luggage_constraints_bp.get('')
def get_all_luggage_constraints() -> Response:
    return make_response(jsonify(luggage_constraints_controller.find_all()), HTTPStatus.OK)


@luggage_constraints_bp.post('')
def create_luggage_constraints() -> Response:
    content = request.get_json()
    item = LuggageConstraints.create_from_dto(content)
    luggage_constraints_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@luggage_constraints_bp.get('/<int:item_id>')
def get_luggage_constraints(item_id: int) -> Response:
    return make_response(jsonify(luggage_constraints_controller.find_by_id(item_id)), HTTPStatus.OK)


@luggage_constraints_bp.put('/<int:item_id>')
def update_luggage_constraints(item_id: int) -> Response:
    content = request.get_json()
    item = LuggageConstraints.create_from_dto(content)
    luggage_constraints_controller.update(item_id, item)
    return make_response("luggage_constraints updated", HTTPStatus.OK)


@luggage_constraints_bp.patch('/<int:item_id>')
def patch_luggage_constraints(item_id: int) -> Response:
    content = request.get_json()
    luggage_constraints_controller.patch(item_id, content)
    return make_response("luggage_constraints updated", HTTPStatus.OK)


@luggage_constraints_bp.delete('/<int:item_id>')
def delete_luggage_constraints(item_id: int) -> Response:
    luggage_constraints_controller.delete(item_id)
    return make_response("progress deleted", HTTPStatus.OK)