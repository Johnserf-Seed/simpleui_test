cls
del db.sqlite3
rmdir /S /Q oj\migrations 
rmdir /S /Q oj\__pycache__
rmdir /S /Q online_judge\__pycache__
python manage.py makemigrations oj
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
python manage.py runscript load_data
