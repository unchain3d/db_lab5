from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import street_adress_controller
from laba4.app.my_project.auth.domain.orders.street_adress import StreetAdress

street_adress_bp = Blueprint('street_adress', __name__, url_prefix='/street_adress')


@street_adress_bp.get('')
def get_all_street_adresses() -> Response:
    return make_response(jsonify(street_adress_controller.find_all()), HTTPStatus.OK)


@street_adress_bp.post('')
def create_street_adress() -> Response:
    content = request.get_json()
    item = StreetAdress.create_from_dto(content)
    street_adress_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@street_adress_bp.get('/<int:item_id>')
def get_street_adress(item_id: int) -> Response:
    return make_response(jsonify(street_adress_controller.find_by_id(item_id)), HTTPStatus.OK)


@street_adress_bp.put('/<int:item_id>')
def update_street_adress(item_id: int) -> Response:
    content = request.get_json()
    item = StreetAdress.create_from_dto(content)
    street_adress_controller.update(item_id, item)
    return make_response("street_adress updated", HTTPStatus.OK)


@street_adress_bp.patch('/<int:item_id>')
def patch_street_adress(item_id: int) -> Response:
    content = request.get_json()
    street_adress_controller.patch(item_id, content)
    return make_response("street_adress updated", HTTPStatus.OK)


@street_adress_bp.delete('/<int:item_id>')
def delete_street_adress(item_id: int) -> Response:
    street_adress_controller.delete(item_id)
    return make_response("street_adress deleted", HTTPStatus.OK)