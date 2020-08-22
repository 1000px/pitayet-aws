from web.api import api
from flask import make_response

@api.after_request
def support_cors(resp):
  res = make_response(resp)
  res.headers['Access-Control-Allow-Origin'] = '*'
  res.headers['Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
  res.headers['Access-Control-Allow-Methods'] = 'GET, POST'
  return res