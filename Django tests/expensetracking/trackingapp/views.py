from django.shortcuts import render, redirect
from trackingapp.forms import ExpenseForm
from trackingapp.models import Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('manage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def addexpense(request):
    expense = Expense.objects.all().order_by('-date')[:10]
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect('addexpense')
    else:
        form = ExpenseForm()
    context = {
        'form': form,
        'expense': expense
    }
    return render(request, 'addexpense.html', context)


@login_required
def manage(request):
    expense = Expense.objects.all().order_by('-date')
    return render(request, 'manageexpense.html', {'expense': expense})


@login_required
def add_budget(request):
    return render(request, 'addbudget.html')


@login_required
def edit(request, pk):
    obj = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=obj)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('manage')
    return render(request, 'editexpense.html', {'form': form})


@login_required
def delete(request, pk):
    obj = Expense.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('manage')
    return render(request, 'delete.html')
# def show(request):
#     expense = Expense.objects.all()
#     return render(request, 'addexpense.html', {'expense': expense})
