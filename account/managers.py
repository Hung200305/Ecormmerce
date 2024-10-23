from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class UserManager(BaseUserManager):
    # def create_user(self, email, password):

    def _create_user(self, email, password):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise




