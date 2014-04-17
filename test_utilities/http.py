import django.http

def make_request():
  return django.http.HttpRequest()

def make_authenticated_request(user):
  request = make_request()
  request.user = user
  return request