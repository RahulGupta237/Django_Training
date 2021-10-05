
Week 2nd Task
Setting Up The Project Now run the following command in your shell to create a Django project.

django-admin startproject DjangoProject
This will generate a project structure with several directories and python scripts.

├── DjangoProject │ ├── init │ ├── settings │ ├── urls │ ├── wsgi ├── manage

Next Create WebApp Application

cd SolveRahul python manage.py startapp Blog These will create an app named blog in our project.

├── db.sqlite3 ├── DjangoProject │ ├── init │ ├── settings │ ├── urls │ ├── wsgi ├── manage └── WebApp ├── init ├── admin ├── apps ├── migrations │ └── _init ├── models ├── tests └── views

python manage.py migrate python manage.py makemigrations

python manage.py runserver

