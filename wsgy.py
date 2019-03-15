import uwsgi
from flask import Flask
import werkzeug
#!flask/bin/python
from app import app
app.run(debug = True)
#app = Flask(__name__)
@rpc('hello')
def hellorpc(foo, bar):
	return "%s-%s-%s" (foo, bar)
def hello():
	return "Hello World"
uwsgi.register_rpc("hello", hello)
def helloapp(env, start_response):
	start_response('200 Ok', [('Content-Type', 'text/html')])
	return uwsgi.rpc('127.0.0.1:3031', 'hello')
def hello_file(num):
	print "/tmp has been modified !!!"
#thr root: 
#application = ...
uwsgi.register_signal(17, "worker", hello_file)
uwsgi.add_file_monitor(17, "/tmp")
uwsgi.applications = {'': application, '/app': app, '/helloapp': helloapp}
