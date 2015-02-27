migrate:
	./manage.py migrate
	./manage.py syncdb

serve:
	./manage.py runserver

deploy:
	ssh root@104.236.220.241 './update.sh'