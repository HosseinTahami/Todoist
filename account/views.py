# Django Imports

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Inside Project Imports

from .models import User
from .forms import UserRegisterForm


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request, 'account/profile.html', {'user': user})


class UserRegisterView(View):

    template_name = 'account/register.html'
    form_class = UserRegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
