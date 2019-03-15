# env
starting uwsgi fastrouter


if fastrouter not set (as it is at this moment):
uwsgi --ini ser.ini

Start emperor to run on every OS restart:
sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals
sudo ln -s /home/jelena/myuwsgi/ser.ini /etc/uwsgi/vassals/
uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data

virtual hosting (supposing key and crt are made):
uwsgi --subscribe2 key=jelenakocic.in.rs,socket=0,sni_key=key.key,sni_crt=crt.crt

if nginx is used:
location / {
include uwsgi_params;
uwsgi_pass 127.0.0.1:4343;
}
