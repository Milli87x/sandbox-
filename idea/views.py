from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView


def login_page(request):
    form = AuthenticationForm(request, data=(request.POST or None))

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('firstpage')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html', {'form': form})


def search(request):
    return render(request, 'search.html', {'active_page': 'search'})


def explore(request):
    return render(request, 'explore.html', {'active_page': 'explore'})


def profile(request):
    return render(request, 'profile.html', {'active_page': 'profile'})


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['active_page'] = None
        return ctx


class Firstpage(TemplateView):
    template_name = 'firstpage.html'


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['active_page'] = 'home'
        return ctx


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('firstpage')  # fixed
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
