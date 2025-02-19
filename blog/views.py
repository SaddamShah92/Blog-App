from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.core.paginator import Paginator
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj' : page_obj})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "blog_detail.html", {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()    
    return render(request, 'blog_form.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else: 
        form = BlogPostForm(instance=post)

    return render(request, 'blog_form.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')

    return render(request, 'blog_confirm_delete.html', {'post': post})
