python3 db_factory.py
gunicorn  -b 0.0.0.0:8000 -w 3 app:app