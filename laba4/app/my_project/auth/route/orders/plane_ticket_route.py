from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from laba4.app.my_project.auth.controller import plane_ticket_controller
from laba4.app.my_project.auth.domain.orders.plane_ticket import PlaneTicket

plane_ticket_bp = Blueprint('plane_ticket', __name__, url_prefix='/plane_ticket')


@plane_ticket_bp.get('')
def get_all_plane_tickets() -> Response:
    return make_response(jsonify(plane_ticket_controller.find_all()), HTTPStatus.OK)


@plane_ticket_bp.post('')
def create_plane_ticket() -> Response:
    content = request.get_json()
    item = PlaneTicket.create_from_dto(content)
    plane_ticket_controller.create(item)
    return make_response(jsonify(item.put_into_dto()), HTTPStatus.CREATED)


@plane_ticket_bp.get('/<int:item_id>')
def get_plane_ticket(item_id: int) -> Response:
    return make_response(jsonify(plane_ticket_controller.find_by_id(item_id)), HTTPStatus.OK)


@plane_ticket_bp.put('/<int:item_id>')
def update_plane_ticket(item_id: int) -> Response:
    content = request.get_json()
    item = PlaneTicket.create_from_dto(content)
    plane_ticket_controller.update(item_id, item)
    return make_response("plane_ticket updated", HTTPStatus.OK)


@plane_ticket_bp.patch('/<int:item_id>')
def patch_plane_ticket(item_id: int) -> Response:
    content = request.get_json()
    plane_ticket_controller.patch(item_id, content)
    return make_response("plane_ticket updated", HTTPStatus.OK)


@plane_ticket_bp.delete('/<int:item_id>')
def delete_plane_ticket(item_id: int) -> Response:
    plane_ticket_controller.delete(item_id)
    return make_response("plane_ticket deleted", HTTPStatus.OK)