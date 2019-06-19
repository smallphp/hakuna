"""
	请求实现类
	
"""
import re
from mvc.route import Route
from mvc.response import Response
	
class Request():
	
	"""
	init
	"""
	def __init__(self, object):
		self.hakuna = object
		self.controller = 'index'
		self.action = 'index'
		self.params = {}
	
	"""
	路由解析
	@param str path_info
	@return bool
	"""
	def __parse(self, path_info):
		route = Route()
		routeTable = route.get()
		for item in routeTable:
			match = re.match(routeTable[item], path_info)
			if (match):
				self.controller = match.group('controller')
				self.action = match.group('action')
		if self.controller and self.action :
			return True
		return False	
	
	"""

	执行请求
	@param dict environ
	@return str
	"""
	def execute(self, environ):
		response = Response()
		result = self.__parse(environ['PATH_INFO'][1:])
		if (result):
			try:
				controller = __import__(self.hakuna.config['controller_dir']+'.'+self.controller)
				try:
					module = getattr(controller, self.controller)
					try:
						object = getattr(module, self.controller.title())
						try:
							method = getattr(object, self.action)
							response.setContent(method())
						except:
							response.setContent('Class '+self.controller.title()+'  Member Method '+self.action+'  do not exist')
					except:
						response.setContent('class '+self.controller+' not found')
				except:
					response.setContent('controller/'+self.controller+' not found')
			except BaseException:
				response.setContent('controller/'+self.controller+'.py not found')	
		else:
			response.setContent('page not found')	
		return response()	
