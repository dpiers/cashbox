ps ax|grep gunicorn|awk '{print $1}'|xargs kill
sleep 5
/projects/cashbox/venv/bin/gunicorn_django /projects/cashbox
