from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    Profile = models.ImageField(upload_to='pro_pics',blank=False, null=False)
    Address=models.CharField(max_length=300,blank=False,null=False)
    is_doctor = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["first_name","last_name","Profile","email","Address"]
#
#     HostFirstName=models.CharField(max_length=20)
#     HostLastName=models.CharField(max_length=30)
#     HostEmail = models.EmailField(unique=True)
#     HostPhone = models.CharField(max_length=12)
#     HostCity=models.CharField(max_length=25)
#
