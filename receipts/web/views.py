from django.contrib.auth import views as auth_views, login
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from receipts.web.forms import SignUpForm, PassChangeForm, ProfileView


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


def service(request):
    return render(request, 'service.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


class SignUpView(views.CreateView):
    template_name = 'sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url


class SignOutView(auth_views.LogoutView):
    template_name = 'sign-out.html'


def information(request):
    return render(request, 'information.html')


class ProfileUpdate(views.UpdateView):
    form_class = ProfileView
    template_name = 'profile/profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, **kwargs):
        return self.request.user


class PasswordChange(PasswordChangeView):
    form_class = PassChangeForm
    template_name = 'profile/password_change.html'
    success_url = reverse_lazy('index')
