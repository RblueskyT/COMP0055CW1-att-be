# att-be

Group 7 attacker Back End
Learn Django: https://www.djangoproject.com/
Learn Django OAuth Toolkit: https://django-oauth-toolkit.readthedocs.io/en/latest/

## Project setup
```
inside the root folder:
py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip (if needed)
python -m pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations example_api
python manage.py migrate example_api
python manage.py createsuperuser (just use admin:admin)
pip install django-cors-headers
```

### Compiles and hot-reloads for development
```
python manage.py runserver 8001 (please do not change this port)
```
