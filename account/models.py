from cgi import maxlen
from datetime import timezone
from email.policy import default

from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db.models import EmailField
from django.forms import models


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=40 ,unique=True)
    password = models.CharField(max_length=40, blank=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.email


