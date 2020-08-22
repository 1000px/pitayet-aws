from web.api import api
from flask import jsonify, request, url_for
from web.models import User

@api.route('/users/')
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
        page, per_page=20,
        error_out=False
    )
    users = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_users', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_users', page=page+1)
    
    return jsonify({
        'users': [user.to_json() for user in users],
        'prev_url': prev,
        'next_url': next,
        'count': pagination.total
    })

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort(404)

    return user.to_json()