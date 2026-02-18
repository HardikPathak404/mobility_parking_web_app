import os
import django
from mps_application.models import User, Resident

os.environ.setdefault("DJANGO_SETTING_MODULE", "web_project.settings")
django.setup()

def populate_data():
    users = [
        User(first_name='John', last_name='Doe', email='johndoe@example.com', password='11510' , phone_number='1234567890')
    ]

    User.objects.bulk_create(users)