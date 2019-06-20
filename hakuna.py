import os
from mvc.route import Route
from mvc.request import Request
from mvc.response import Response

class Hakuna():

	route = None

	request = None

	response = None 
		
	config = {
		'base_dir': os.getcwd(),
		'controller_dir' : 'controller'
	}

	def __init__(self):
		Hakuna.route = Route()
		Hakuna.request = Request(self)
		Hakuna.response = Response()
	"""
	wsgi
	"""
	def wsgi(self):
		def application(environ, start_response):
			body = self.__web(environ)
			start_response(str(body[1]), body[2])
			return [body[0]]
		return application
	
	"""
	addroute
	"""
	def addRoute(self, path, pattern={}, default={}):
		Hakuna.route.add(path, pattern, default)
	"""
	web
	"""
	def __web(self, environ):
		return Hakuna.request.execute(environ)
