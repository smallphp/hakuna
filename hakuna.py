"""
	python web framework
"""

import os
from hakuna.mvc.route import Route
from hakuna.mvc.request import Request
from hakuna.mvc.response import Response

class Hakuna():
	
	route = request = response = None 
		
	config = {
		'base_dir': os.getcwd(),
		'controller_dir' : 'controller'
	}
	
	"""
	__init__
	"""
	def __init__(self, **kw):
		if Hakuna.route is None:
			Hakuna.route = Route(self)
		if Hakuna.request is None:
			Hakuna.request = Request(self)
		if Hakuna.response is None:
			Hakuna.response = Response(self)
	
	"""
	wsgi application
	"""
	def wsgi(self):
		def application(environ, start_response):
			body = self.__runWeb(environ)
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
	def __runWeb(self, environ):
		return Hakuna.request.execute(environ)
