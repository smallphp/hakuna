class Hakuna():

	import os
	
	config = {
		'base_dir': os.getcwd(),
		'controller_dir' : 'controller'
	}
	
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
	web
	"""
	def __web(self, environ):
		from mvc.route import Route 
		from mvc.request import Request
		request = Request(self)
		return request.execute(environ)
