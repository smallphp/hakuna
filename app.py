def application(environ, start_response):
	start_response('200 ok',[('Content-type','text/html')])
	from mvc.route import Route
	from mvc.request import Request
	route = Route()
	route.add('(<controller>)-(<action>).html',{'controller':'[a-zA-Z]+','action':'[a-zA-Z]+'})
	request = Request()
	return [request.execute(environ)]
