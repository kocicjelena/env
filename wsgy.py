import uwsgi
import django.core.handlers.wsgi
from flask import Flask

import werkzeug
#!flask/bin/python
from app import app
app.run(debug = True)
#app = Flask(__name__)
@rpc('hello')
def hellorpc(arg1, arg2, arg3):
	return "%s-%s-%s" (arg3, arg2, arg1)
  def hello():
	return "Hello World"
	uwsgi.register_rpc("hello", hello)
def helloapp(env, start_response):
	start_response('200 Ok', [('Content-Type', 'text/html')])
	return uwsgi.rpc('10.0.0.2:3031', 'hello')
def hello_file(num):
	print "/tmp has been modified !!!"
uwsgi.register_signal(17, "worker", hello_file)
uwsgi.add_file_monitor(17, "/tmp")
uwsgi.applications = {'': application, '/app': app,}
