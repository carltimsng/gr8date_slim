web: gunicorn core.wsgi --log-file - --bind 0.0.0.0:${PORT:-8000}
release: python manage.py migrate && python manage.py ensure_superuser && python manage.py loaddata fixtures/initial_data.json.gz.gz && python manage.py load_seed_media && python manage.py collectstatic --noinput
