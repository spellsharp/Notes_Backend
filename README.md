# Set up
- Clone the repo using `git clone https://github.com/spellsharp/Notes_Backend.git`
- `cd Notes_Backend` into the cloned repo.
- Run `python manage.py migrate` to make the migrations. After this you should see a db.sqlite3 file.
- Run `python manage.py runserver` to run the Django server locally at localhost:8000
- Run `python manage.py createsuperuser` and follow the steps to create a super user with admin access.
- Visit https://localhost:3000/admin and use the previous credentials to log into the admin page.
- Make new Notes or Tags and experiment.