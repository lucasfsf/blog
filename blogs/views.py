from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for the Blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Add a new Blog Post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post"""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

