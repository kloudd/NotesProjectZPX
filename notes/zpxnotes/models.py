from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from datetime import datetime


class Notes(models.Model):
    data=models.CharField(max_length=100)
    author=models.ForeignKey(User)
    created_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(default=datetime.now())
