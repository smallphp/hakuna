# hakuna 一个简单的Python Web框架

环境 python3  

setup 1)  
运行
/usr/local/python/bin/uwsgi uwsgi.ini  

setup 2)  

测试GET方式    
curl 127.0.0.1:8080  
结果  
<h1>hakuna matata!</h1>  

测试POST方式  
curl 127.0.0.1:8080 -d '{"name":"leon"}'  
结果  
{'name': 'leon'}  


路由实现原理  
每个路由包含一个部分 uri pattern default 三部分，如下示例  
(<controller>)-(<action>) {"controller":"[a-z]+","action":"[a-c]+"} {"controller":"index","action":"index"}  
Route类将uri与pattern生一个正则表达是如上生成如下    
(?P<controller>[a-z])-(?P<action>[a-c]+)  
正则表达式中 (?P<组名>) 来自定义分组名称，php中可以不需要P，如果在捕获的组名中没有包含controller、action一起其他param，从路由第三个元素中获取
  
上面的路由表示  
uri匹配a-z控制器的controller，action只能是a-c。如果没有匹配到，则默认是 index 控制器 index action
