# Django Imports

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View


# Inside Project Imports

from .forms import UserRegisterForm, UserLoginForm
from .models import User


class ProfileView(LoginRequiredMixin, View):

    def setup(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if self.user.is_authenticated and self.user.id != request.user.id:
            messages.error(
                request, "This Profile Does Not Belong To You..!", "danger")
            return redirect('account:profile', request.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'account/profile.html', {'user': self.user})


class UserRegisterView(View):

    template_name = 'account/register.html'
    form_class = UserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:profile', request.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                email=cd['email'],
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                password=cd['password'],
            )
            messages.success(
                request, 'Account Created Successfully..!', 'success')
        return redirect('core:home')


class UserLoginView(View):

    template_name = 'account/login.html'
    from_class = UserLoginForm

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:profile', pk=request.user.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.from_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['authenticator'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'Logged In Successfully..!', 'success')
                if self.next:
                    return redirect(self.next)
                return redirect('core:home')
            messages.error(
                request, 'Wrong Password or Authenticator..!', 'danger')
            return redirect('core:home')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logged Out Successfully..!', 'warning')
        return redirect('core:home')
