import uwsgi
from flask import Flask
import werkzeug
#!flask/bin/python
from app import app
app.run(debug = True)
domains['jelenakocic.in.rs'] = {'nodes': ('127.0.0.1:3031', '192.168.43.1:4343'), 'node':
˓ → 0}
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
def get(key):
	if key not in domains:
		return DEFAULT_NODE
	# get the node to forward requests to
	nodes = domains[key]['nodes']
	current_node = domains[key]['node']
	value = nodes[current_node]
	# round robin :P
	next_node = current_node + 1
	if next_node >= len(nodes):
		next_node = 0
		domains[key]['node'] = next_node
		return value
#thr root: 
#application = ...
uwsgi.register_signal(17, "worker", hello_file)
uwsgi.add_file_monitor(17, "/tmp")
uwsgi.applications = {'': application, '/app': app, '/helloapp': helloapp}
