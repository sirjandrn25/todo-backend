web: waitress-serve --port=$PORT todo_project.wsgi:application
web: gunicorn todo_project.wsgi:application --log-file - --log-level debug