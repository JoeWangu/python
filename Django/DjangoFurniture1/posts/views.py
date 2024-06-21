from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q
from comments.models import Comment
from comments.forms import CommentForm
# from django.contrib.contenttypes.models import ContentType


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'successfully created')
        return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request, 'post_form.html',context)

def posts_detail(request, id=None): #retrieve
    # instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id = id)
    if instance.draft or instance.publish > timezone.now():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    share_string = quote_plus(instance.content)

    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            # Create Comment object
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'Success! comment posted')
            # comment_form = CommentForm()
            return HttpResponseRedirect('')
    else:
        comment_form = CommentForm()


    context = {
        'title': instance.title,
        'instance': instance,
        'share_string': share_string,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'post_detail.html',context)


#paginating - manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links.
# It does all the heavy lifting of actually splitting a QuerySet into Page objects.

#return the list items

def posts_list(request):
    today = timezone.now()
    queryset_list = Post.objects.active()   #filter(draft=False).filter(publish__lte=timezone.now())
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()   #.order_by('-timestamp')
    
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 3) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj_items = page_obj.object_list
    
    context = { 
        'object_list': page_obj_items,
        'title': 'list',
        'page_obj': page_obj,
        'today': today,
    }
    return render(request, 'post_list.html',context)


#paginating done

def posts_update(request, id = None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, 'successfully updated')
        return HttpResponseRedirect('/')
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'post_form.html',context)


def posts_delete(request, id = None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id = id)
    instance.delete()
    messages.success(request, 'successfully deleted')
    return redirect('/')


# posts_detail

    # initial_data = {
    #     'content_type': instance.get_content_type,
    #     'object_id': instance.id,
    # }
    # form = CommentForm(request.POST or None, initial=initial_data)
    # if form.is_valid():
    #     c_type = form.cleaned_data.get('content_type')
    #     content_type = ContentType.objects.get(model = c_type)
    #     obj_id = form.cleaned_data.get('object_id')
    #     content_data = form.cleaned_data.get('content')
    #     new_comment, created = Comment.objects.get_or_create(
    #         user = request.user,
    #         content_type = content_type,
    #         object_id = obj_id,
    #         content = content_data
    #     )
    #     if created:
    #         print('yes it worked')

    # comments = instance
    # comments = Comment.objects.filter_by_instance(instance)

    # context

        # 'comments': comments,
        # 'comment_form': form,

