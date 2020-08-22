from . import api
from flask import request, jsonify, render_template

@api.errorhandler(404)
def uri_not_found(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Not found.'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

@api.errorhandler(401)
def uri_not_allowed(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Not allowed.'})
        response.status_code = 401
        return response
    return render_template('401.html'), 401 # 临时