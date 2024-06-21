from django.shortcuts import render, redirect
from userprofile.forms import UserForm
from django.contrib.auth import login, authenticate
from .models import Profile

# Create your views here.
def home(request):
    profile = Profile.objects.all()
    context = {
    'profile': profile,
    }
    return render(request, 'userprofile/home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'register/register.html', {'form': form})