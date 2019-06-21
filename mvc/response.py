"""
	响应实现类
"""
class Response():
	
	#hakuna
	hakuna = None
			
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
	def __init__(self, hakuna):
		Response.hakuna = hakuna
		self.content = ''
		self.headers = [('Content-type','text/html')]
	
	"""
	setHeaders
	"""	
	def setHeaders(self, headers=[]):
		self.headers = headers

	
	"""
	setContent
	"""
	def setContent(self, content=''):
		self.content = content
	
	"""
	__call__
	"""
	def __call__(self):
		return (str(self.content).encode('utf-8'), 200, self.headers)
	
	
