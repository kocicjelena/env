# env
starting uwsgi fastrouter
if nginx is used:
location / {
include uwsgi_params;
uwsgi_pass 127.0.0.1:3031;
}
