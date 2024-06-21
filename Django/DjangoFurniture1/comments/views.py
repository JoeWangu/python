from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

@login_required #(login_url='/login/') --> you dont need this if you added the url in settings

def comment_delete(request, id= None):
    obj = get_object_or_404(Comment, id=id)
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if obj.user != request.user:
        return HttpResponse('<h1>You do not have permission to do this</h1>')

        # raise Http404

    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Comment successfully deleted')
        return HttpResponseRedirect('/')

    context = {
        'object': obj,
    }

    return render(request, 'confirm_delete.html', context)


def comment_list(request,id=None):
    queryset_list = Comment.objects.filter(post=id)   #.order_by('-timestamp')

    context = {
        'comments': queryset_list,
    }
    return render(request, 'comment_list.html',context)

def comment_detail(request, id=None):
    comment = get_object_or_404(Comment, id=id)

    context = {
        'com': comment,
    }
    return render(request, 'comment_detail.html', context)