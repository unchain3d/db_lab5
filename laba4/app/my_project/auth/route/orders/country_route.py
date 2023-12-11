from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import country_controller
from laba4.app.my_project.auth.domain.orders.country import Country

country_bp = Blueprint('country', __name__, url_prefix='/country')


@country_bp.get('')
def get_all_countries() -> Response:
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)


@country_bp.post('')
def create_countries() -> Response:
    content = request.get_json()
    item = Country.create_from_dto(content)
    country_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@country_bp.get('/<int:item_id>')
def get_country(item_id: int) -> Response:
    return make_response(jsonify(country_controller.find_by_id(item_id)), HTTPStatus.OK)


@country_bp.put('/<int:item_id>')
def update_country(item_id: int) -> Response:
    content = request.get_json()
    item = Country.create_from_dto(content)
    country_controller.update(item_id, item)
    return make_response("country updated", HTTPStatus.OK)


@country_bp.patch('/<int:item_id>')
def patch_country(item_id: int) -> Response:
    content = request.get_json()
    country_controller.patch(item_id, content)
    return make_response("country updated", HTTPStatus.OK)


@country_bp.delete('/<int:item_id>')
def delete_country(item_id: int) -> Response:
    country_controller.delete(item_id)
    return make_response("country deleted", HTTPStatus.OK)
