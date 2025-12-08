from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import profile as ProfileModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib import admin


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
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            try:
                profile, created = ProfileModel.objects.get_or_create(user=user, defaults={'email': email})
                if not created and getattr(profile, 'email', None) != email:
                    profile.email = email
                    profile.save()
            except Exception:
                pass

            auth_login(request, user)
            return redirect('firstpage')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def my_profile(request):
    return redirect('profile_detail', username=request.user.username)

def profile_detail(request, username):
    User = get_user_model()
    user_obj = get_object_or_404(User, username=username)
    profile = getattr(user_obj, 'profile', None)
    return render(request, 'profile.html', {
        'profile_user': user_obj,
        'profile': profile,
    })
