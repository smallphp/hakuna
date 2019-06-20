class Index():
	def index(self):
		if self.request.method == 'POST':
			post = self.request.post()
			return post	
		else :
			return '<h1>hukuna matata</h1>'
