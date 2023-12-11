from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import airline_company_controller
from laba4.app.my_project.auth.domain.orders.airline_company import AirlineCompany

airline_company_bp = Blueprint('airline_company', __name__, url_prefix='/airline_company')


@airline_company_bp.get('')
def get_all_airc() -> Response:
    return make_response(jsonify(airline_company_controller.find_all()), HTTPStatus.OK)


@airline_company_bp.post('')
def create_airc() -> Response:
    content = request.get_json()
    airline_company = AirlineCompany.create_from_dto(content)
    airline_company_controller.create(airline_company)
    return make_response(jsonify(airline_company.put_into_dto()), HTTPStatus.CREATED)


@airline_company_bp.get('/<int:airline_company_id>')
def get_airc(airline_company_id: int) -> Response:
    return make_response(jsonify(airline_company_controller.find_by_id(airline_company_id)), HTTPStatus.OK)


@airline_company_bp.put('/<int:airline_company_id>')
def update_airc(airline_company_id: int) -> Response:
    content = request.get_json()
    airline_company = AirlineCompany.create_from_dto(content)
    airline_company_controller.update(airline_company_id, airline_company)
    return make_response("AirlineCompany updated", HTTPStatus.OK)


@airline_company_bp.patch('/<int:airline_company_id>')
def patch_airc(airline_company_id: int) -> Response:
    content = request.get_json()
    airline_company_controller.patch(airline_company_id, content)
    return make_response("AirlineCompany updated", HTTPStatus.OK)


@airline_company_bp.delete('/<int:airline_company_id>')
def delete_airc(airline_company_id: int) -> Response:
    airline_company_controller.delete(airline_company_id)
    return make_response("AirlineCompany deleted", HTTPStatus.OK)
