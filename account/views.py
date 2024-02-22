# Django Imports

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# Inside Project Imports

from .models import User
from . import forms


class UserProfileView(LoginRequiredMixin, View):

    template_name = 'account/profile.html'
    form_class = forms.UserProfileForm

    def setup(self, request, *args, **kwargs):
        self.user_instance = User.objects.get(pk=kwargs['user_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        user = self.user_instance
        form = self.form_class(instance=request.user)
        if not user == request.user:
            messages.error(
                request, "This profile does not belong to you..!", 'danger')
            return redirect('account:user_profile', request.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = self.user_instance
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = self.user_instance
        form = self.form_class(request.POST, request.FILES, instance=user)
        if form.is_valid():
            new_user = form.save()
            messages.success(
                request, 'Your info updated successfully', 'success')
            return redirect('account:user_profile', request.user.id)
