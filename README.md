# Date invitation

A small Django site for the date invitation. It stores responses in a local SQLite database (`db.sqlite3`).

## Run locally

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment, then install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Create the database tables and an admin account:

   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Start the site:

   ```powershell
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ for the invitation. Sign in with the superuser account at http://127.0.0.1:8000/admin/, then open http://127.0.0.1:8000/responses/ to review answers. The response page requires a staff login.

Responses are recorded when someone chooses “Maybe another time” or submits the final review page. SQLite data is stored in `db.sqlite3` and is excluded from Git.
