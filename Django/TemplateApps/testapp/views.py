from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from testapp.models import Student


# Create your views here.
def home(request):
    data = Student.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'index.html', context)


def insertData(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        query = Student(name=username, email=email, age=age, gender=gender)
        query.save()
        return redirect('/')
    return render(request, 'index.html')


def updateData(request, id):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
        return redirect('/')
    else:
        d = Student.objects.get(id=id)
        return render(request, 'edit.html', {'d': d})


def deleteData(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('/')
    # return render(request, 'index.html')
