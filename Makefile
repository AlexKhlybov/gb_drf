run:
	python3 manage.py runserver

cleandb:
	rm -rf ./apps/todos/migrations/00*
	rm -rf ./apps/users/migrations/00*

	rm -rf ./db.sqlite3

	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py dbimport

refac:
	isort .
	black -l120 .
