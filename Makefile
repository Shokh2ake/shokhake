mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

migrate:
	python3 manage.py createsuperuser

check:
	isort .
	flake8 .