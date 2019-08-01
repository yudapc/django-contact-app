# Contact app

This project for learning to create contact app using django


## Step by Step

### Create virtual env with name `venv`

`python3 -m venv venv`

### Activate virtual env:

`source venv/bin/activate`

### Install dependencies

`pip install -r requirement.txt`

### Initial project with name `app`

`django-admin startproject app .`

### Setup `app/settings.py`:

```
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
TIME_ZONE = 'Asia/Jakarta'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### Run migration

`python manage.py migrate`

### Run server and run on port 8000 -> `http://localhost:8000`

`python manage.py runserver`

### Generate new module

`python manage.py startapp <module-name>`

### Edit file <module-name>/models.py

```
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def __str__(self):
        return self.full_name()
```

### Make migration module

`python manage.py makemigrations <module-name>`

### Run migration module

`python manage.py migrate <module-name>`

Source: 
https://medium.com/@siddharthshringi/how-i-made-my-first-django-app-4ede65c9b17f
