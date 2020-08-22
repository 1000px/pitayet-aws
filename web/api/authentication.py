from flask_httpauth import HTTPBasicAuth
from flask import g
import re

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(key, password):
    if key == '':
        return False
    
    pat = r'^[A-Za-z0-9_]+@[A-Za-z0-9_-]+(\.[A-Za-z0-9_-]+)+$'
    if re.search(pat, key) is None:
        user = User.query.filter_by(username=key).first()
    else:
        user = User.query.filter_by(email=key).first()
    
    if not user:
        return False

    g.current_user = user

    return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')  