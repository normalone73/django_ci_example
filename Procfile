# Medhat, run this command for one time from Heroku Exec (SSH Tunneling) revised!
release: python manage.py syncdb --migrate --noinput --all
# release: python manage.py migrate
# Medhat
web: gunicorn django_ci_example.wsgi
