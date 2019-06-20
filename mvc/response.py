"""
	响应实现类
"""
class Response():
	
	"""
	httpState
	"""
	httpState = {
		200:'ok',
		404:'page not found'
	}

	"""
	__init__
	"""
	def __init__(self):
		self.content = ''
		self.headers = [('Content-type','text/html')]
	
	def setHeaders(self, headers=[]):
		self.headers = headers
	
	def setContent(self, content=''):
		self.content = content
	
	def __call__(self):
		return (str(self.content).encode('utf-8'), 200, self.headers)
	
	
