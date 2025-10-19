from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from pprint import pprint

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('created_at')
    pprint(list(posts.values()))
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_create(request):
    form = PostForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html',{'form':form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if(form.is_valid()):
        form.save()
        return redirect('post_list')
    return render(request,'blog/post_form.html',{'form':form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if(request.method == 'POST'):
        post.delete()
        return redirect('post_list')
    return render(request,'blog/post_confirm_delete.html',{'post':post})