from django.shortcuts import render, redirect
from userform.forms import UserForm
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request, 'userform/home.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})