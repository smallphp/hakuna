"""
	请求实现类
	
"""
import re
	
class Request():
	
	__environ = {}
	
	"""
	init
	"""
	def __init__(self, object):
		self.hakuna = object
		self.controller = ''
		self.action = ''
		self.params = {}
		self.method = 'GET'
	
	"""
	路由解析
	@param str path_info
	@return bool
	"""
	def __parse(self, path_info):
		if (path_info) :
			routeTable = self.object.route.get()
			for item in routeTable:
				match = re.match(routeTable[item], path_info)
				if (match):
					self.controller = match.group('controller')
					self.action = match.group('action')
			if self.controller and self.action :
				return True
		else: 
			self.controller = self.action = 'index'
			return True
	
	"""

	执行请求
	@param dict environ
	@return str
	"""
	def execute(self, environ):
		self.__environ = environ
		self.method = environ['REQUEST_METHOD']
		response = self.hakuna.response
		result = self.__parse(environ['PATH_INFO'][1:])
		if (result):
			try:
				controller = __import__(self.hakuna.config['controller_dir']+'.'+self.controller)
				print(self.hakuna.config)
				try:
					module = getattr(controller, self.controller)
					try:
						object = getattr(module, self.controller.title())
						object.request = self
						try:
							method = getattr(object, self.action)
							response.setContent(method(object))
						except  BaseException as err:
							#response.setContent('Class '+self.controller.title()+'  Member Method '+self.action+'  do not exist')
							response.setContent(format(err))
					except:
						response.setContent('class '+self.controller+' not found')
				except:
					response.setContent('controller/'+self.controller+' not found')
			except BaseException:
				response.setContent('controller/'+self.controller+'.py not found')	
		else:
			response.setContent('page not found')	
		return response()

	"""
	post 获取POST数据
	@parma str key
	@return mixed
	"""
	def post(self, key=None):
		if self.method == 'POST':
			leng = self.__environ.get('CONTENT_LENGTH');
			if leng is None:
				leng = 0
			data = self.__environ.get('wsgi.input').read(int(leng))
			data = eval(data.decode('utf-8'))
			if key is not None:
				if key in data:
					return data[key]
				else :
					return None
			return data
		return None
