from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import client_history_controller
from laba4.app.my_project.auth.domain.orders.client_history import ClientHistory

client_history_bp = Blueprint('client_history', __name__, url_prefix='/client_history')


@client_history_bp.get('')
def get_all_client_histories() -> Response:
    return make_response(jsonify(client_history_controller.find_all()), HTTPStatus.OK)


@client_history_bp.post('')
def create_client_history() -> Response:
    content = request.get_json()
    item = ClientHistory.create_from_dto(content)
    client_history_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@client_history_bp.get('/<int:item_id>')
def get_client_history(item_id: int) -> Response:
    return make_response(jsonify(client_history_controller.find_by_id(item_id)), HTTPStatus.OK)


@client_history_bp.put('/<int:item_id>')
def update_client_history(item_id: int) -> Response:
    content = request.get_json()
    item = ClientHistory.create_from_dto(content)
    client_history_controller.update(item_id, item)
    return make_response("ClientHistory updated", HTTPStatus.OK)


@client_history_bp.patch('/<int:item_id>')
def patch_client_history(item_id: int) -> Response:
    content = request.get_json()
    client_history_controller.patch(item_id, content)
    return make_response("client_history updated", HTTPStatus.OK)


@client_history_bp.delete('/<int:item_id>')
def delete_client_history(item_id: int) -> Response:
    client_history_controller.delete(item_id)
    return make_response("client_history deleted", HTTPStatus.OK)
