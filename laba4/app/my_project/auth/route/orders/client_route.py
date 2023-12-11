from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import client_controller
from laba4.app.my_project.auth.domain.orders.client import Client

client_bp = Blueprint('client', __name__, url_prefix='/client')


@client_bp.get('')
def get_all_clients() -> Response:

    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)


@client_bp.post('')
def create_client() -> Response:
    content = request.get_json()
    item = Client.create_from_dto(content)
    client_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@client_bp.get('/<int:item_id>')
def get_client(item_id: int) -> Response:

    return make_response(jsonify(client_controller.find_by_id(item_id)), HTTPStatus.OK)


@client_bp.put('/<int:item_id>')
def update_client(item_id: int) -> Response:

    content = request.get_json()
    item = Client.create_from_dto(content)
    client_controller.update(item_id, item)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.patch('/<int:item_id>')
def patch_client(item_id: int) -> Response:

    content = request.get_json()
    client_controller.patch(item_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.delete('/<int:item_id>')
def delete_client(item_id: int) -> Response:

    client_controller.delete(item_id)
    return make_response("Client deleted", HTTPStatus.OK)