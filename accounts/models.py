from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db.models.base import ModelState
from .managers import MyUserManager
# Create your models here.



class User(BaseUserManager):
    email = models.EmailField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']


    def __str__(self):
        return self.email

    
    def has_perm(self, perm, obj=None):
        return True


    def has_moudle_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin



class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='1.jpg')
    