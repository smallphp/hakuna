"""
	响应实现类
"""
class Response():
	"""
	__init__
	"""
	def __init__(self):
		self.content = ''
		self.headers = []
	
	def setHeaders(self, headers=[]):
		self.headers = headers
	
	def setContent(self, content=''):
		self.content = content
	
	def __call__(self):
		return self.content.encode('utf-8')
	
	
