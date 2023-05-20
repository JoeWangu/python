from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
# from django.views import generic

# Create your views here.
def home(request):
    title = 'Registry'
    context = {
        'title': title,
    }
    return render(request, 'home.html', context)

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def signup_login(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        login_form = AuthenticationForm(request, data=request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('home')
        elif login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        signup_form = CustomUserCreationForm()
        login_form = AuthenticationForm()
    return render(request, 'signup_login.html', {'signup_form': signup_form, 'login_form': login_form})
