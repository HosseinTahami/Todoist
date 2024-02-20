from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import BaseBackend
# Inside Project Imports

from accounts.models import User


class EmailBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None

        except ObjectDoesNotExist:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist:
                return None

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
