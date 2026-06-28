# Pharmacy Inventory System

A Django-based pharmacy inventory management application for tracking medicines, expiry dates, stock levels, and supplier details.

## Features

- User authentication with login/logout
- Dashboard with stock summary and recent entries
- Medicine list with search support
- Add, edit, and delete medicine records
- View expired medicines and medicines expiring within 30 days
- Uses SQLite by default, with optional database configuration via `dj_database_url`

## Tech stack

- Python 3
- Django 6.0.6
- SQLite (default)
- Whitenoise for static file support
- dj-database-url for environment-based database configuration

## Setup

From the project root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> If `pip install -r requirements.txt` fails due to encoding, convert the file to UTF-8 before installing.

## Database setup

Run migrations:

```bash
python manage.py migrate
```

Create a superuser if you want to access the Django admin:

```bash
python manage.py createsuperuser
```

## Run the project

Start the development server:

```bash
python manage.py runserver
```

Open the app in your browser:

```
http://127.0.0.1:8000/
```

## App URLs

- `/login/` - login page
- `/logout/` - logout
- `/dashboard/` - inventory dashboard
- `/medicines/` - medicine listing
- `/medicines/add/` - add medicine
- `/medicines/expired/` - expired medicines
- `/medicines/expiring/` - expiring soon medicines
- `/admin/` - Django admin site

## Notes

- The project uses `pharmacy.settings` as the Django settings module.
- The default database is `sqlite:///db.sqlite3`.
- To enable debug mode locally, set `DEBUG=True` in the environment before starting the server.

## License

This repository does not include a license file.
