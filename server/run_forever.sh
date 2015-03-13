#! /bin/bash

sudo killall python
sudo nohup python manage.py runserver >& server.log &

CHECK="$(pidof sudo nohup python manage.py runserver | wc -w)"
while true; do
	if (("$CHECK" != "0")); then
		sleep 5
		break
	else
		sudo killall python
		sleep 1
		sudo nohup python manage.py runserver >& server.log &
	fi
	CHECK="$(pidof sudo nohup python manage.py runserver | wc -w)"
done


