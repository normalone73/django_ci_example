# Medhat, run this command for one time from Heroku Exec (SSH Tunneling) revised!
release: exec python manage.py syncdb --migrate --noinput
# release: python manage.py migrate
# Medhat
web: gunicorn django_ci_example.wsgi
