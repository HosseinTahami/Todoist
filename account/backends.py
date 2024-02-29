# Django Imports
from django.contrib.auth.backends import BaseBackend
from django.shortcuts import get_object_or_404

# Inside Project Imports
from .models import User


class EmailBackend(BaseBackend):

    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password=password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
