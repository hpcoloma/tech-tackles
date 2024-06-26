from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Profile models
class Profile(models.Model):
    ROLES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('IT Support', 'IT Support'),
        
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default='User')


    def __str__(self):
        return self.user.username

# Ticket model
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Open')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.subject


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment by {self.user} on {self.ticket.subject}"


