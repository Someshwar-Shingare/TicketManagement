from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ticket(models.Model):
    CATEGORY = (
        ('Travelling', 'Travelling'),
        ('Movie', 'Movie'),
        ('Tourism', 'Tourism')
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Booked', 'Booked'),
        )
    price = models.CharField(max_length=32)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date = models.DateField(auto_now_add=True)
    current_user = models.ForeignKey(User,on_delete=models.CASCADE)




