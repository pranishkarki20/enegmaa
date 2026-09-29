# Enigma Tech Club

A React landing page with a Django REST API scaffold for Enigma, a student-led university technology club.

## Frontend

```powershell
npm install
npm run dev
```

## Backend

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

The API exposes `GET /api/events/`, `GET /api/projects/`, and `POST /api/join/` (`{"email":"you@example.com"}`). Events and projects are managed from `/admin/` and only published records appear in the public lists. Before deployment, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false`, `DJANGO_ALLOWED_HOSTS`, and `CORS_ALLOWED_ORIGINS`.
