# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (('admin', 'Admin'), ('customer', 'Customer'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

class PolicyHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

class PolicyRequest(models.Model):
    STATUS_CHOICES = (('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'))
    policy_holder = models.ForeignKey(PolicyHolder, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
