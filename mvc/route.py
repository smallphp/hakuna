"""
	路由实现类
	example 1:
		route.add('(<controller>)-(<action>).html', {'controller':'news','action':'list'})
		path_info = /news-list.html
		controller = news
		action = list
	example 2:
		route.add('(<new_id>).html', {'new_id':'[1-9][0-9]+'},{'controller':'news','action':'details'})
		path_info = /1.html
		controller = news
		action = details
		new_id = 1
"""
class Route():
	
	#路由表
	__routeTables = {}
	
	"""
	添加路由
	param str path
	param dict pattern
	param dict default
	"""	
	def add(self, path, pattern={}, default={}):
		if path not in Route.__routeTables:
			Route.__routeTables[path] = self.__parse(path, pattern, default)
			return True
		return False

	"""
	获取路由
	param void
	return dict
	"""
	def get(self):
		return Route.__routeTables
		
	"""
	解析路由
	param str path
	param dict pattern
	param dict default
	return str
	"""
	def __parse(self, path, pattern, default):
		import re
		string = re.sub("(?<=[(])(?=[<])", '?P', path)
		groups = re.findall("(?:(?<=[(][?][P][<])([a-zA-z]+)(?=[>][)]))+", string)
		for group in groups:
			if group in pattern:
				string = re.sub('(?<='+group+'[>])(?=[)])', pattern[group], string)
			else:
				if group in default:
					string = re.sub('(?<='+group+'[>])(?=[)])', default[group], string)
				else:
					string = re.sub('(?<='+group+'[>])(?=[)])', '[a-zA-z]+', string)
		return string
