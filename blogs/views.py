from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for the Blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

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
