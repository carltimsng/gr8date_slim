web: gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate && \
  DJANGO_SUPERUSER_USERNAME=carlsng \
  DJANGO_SUPERUSER_EMAIL=admin@example.com \
  DJANGO_SUPERUSER_PASSWORD='MyNewPassword123' \
  python manage.py createsuperuser --noinput || true && \
  python manage.py loaddata fixtures/initial_data.json.gz && \
  python manage.py normalize_profiles && \
  python manage.py collectstatic --noinput
