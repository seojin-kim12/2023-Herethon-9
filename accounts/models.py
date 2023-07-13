from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

"""class CustomUser(models.Model):
    custom_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=16, unique=True) """

class CustomUserManager(BaseUserManager):
    def create_user(self, custom_id, password=None, **extra_fields):
        if not custom_id:
            raise ValueError("Custom ID must be set")
        user = self.model(custom_id=custom_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def get_username(self, custom_id): #호환성 위해 추가 -혜승
        return custom_id

class CustomUser(AbstractBaseUser):
    custom_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=16, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'custom_id'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Meta:
    db_table ='custom_user'
    verbose_name ='custom_user'
    verbose_name_plural = 'custom_user'
