# hakuna matata

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
