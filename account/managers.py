# Django Imports
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    @staticmethod
    def check_field(field, field_name):
        if not field:
            raise ValueError(f"Must include {field_name}..!")

    def create_user(self, first_name, last_name, email, password):

        self.check_field(email, 'Email')
        self.check_field(first_name, 'First Name')
        self.check_field(last_name, 'Last Name')
        self.check_field(password, 'Password')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):

        user = self.create_user(
            first_name, last_name, email, password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
