web: gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
release: |
  export DJANGO_SUPERUSER_USERNAME=carlsng
  export DJANGO_SUPERUSER_EMAIL=admin@example.com
  export DJANGO_SUPERUSER_PASSWORD='MyNewPassword123'
  python manage.py migrate
  python manage.py createsuperuser --noinput || true
  python manage.py loaddata fixtures/initial_data.json.gz
  python manage.py import_profiles_csv --csv fixtures/profiles_owner_merged.csv
  python manage.py normalize_profiles
  python manage.py load_seed_media
  python manage.py collectstatic --noinput
