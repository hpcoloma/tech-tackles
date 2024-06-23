from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('IT Support', 'IT Support'),
        
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default='User')


    # def __str__(self):
    #     retur self.user.username
