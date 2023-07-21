from django.shortcuts import render

# Create your views here.
def dashboard(request):
    title = 'Dashboard'
    context = {
        'title': title,
    }
    return render(request, 'rest/dashboard.html', context)