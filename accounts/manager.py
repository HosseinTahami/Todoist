from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    @staticmethod
    def required(field, field_name):
        if not field:
            raise ValueError(f'{field_name} Required..!')

    def create_user(self, email, first_name, last_name, password):

        self.required(email, 'Email')
        self.required(first_name, 'First name')
        self.required(last_name, 'Last name')
        self.required(password, 'Password')

        user = self.model(
            email = self.normalize_email(email)
            first_name = first_name
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password):

        superuser = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser