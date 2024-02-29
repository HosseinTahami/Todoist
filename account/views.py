from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import User


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        return render(request, 'account/profile.html', {'user': user})
