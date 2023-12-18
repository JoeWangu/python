from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from dataapp.models import Patient
from dataapp.forms import PatientForm


def index(request):
    return render(request, 'index.html')


@login_required
def create(request):
    form = PatientForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('retrieve')
    else:
        form = PatientForm()
    context = {
        'form': form,
    }
    return render(request, 'dataentry.html', context)


@login_required
def retrieve(request):
    records = Patient.objects.all()
    context = {
        'records': records,
    }
    return render(request, 'retrieve.html', context)


@login_required
def update(request, pk):
    details = Patient.objects.get(id=pk)
    form = PatientForm(instance=details)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=details)
        if form.is_valid():
            form.save()
        else:
            form = PatientForm()
        return redirect('retrieve')
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


@login_required
def delete(request, pk):
    data = Patient.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('retrieve')
    return render(request, 'delete.html')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('retrieve')
    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)
