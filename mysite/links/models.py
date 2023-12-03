from django.db import models

# Create your models here.


class Link(models.Model):
    raw_link = models.CharField(max_length=100)
    link_name = models.CharField(max_length=30)


# python manage.py makemigrations //makes file
# python manage.py migrate //run after model creation
