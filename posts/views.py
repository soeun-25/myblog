from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, Content=content)
    return redirect('posts:main')

def main(request):
    posts = Post.objects.all()
    return render(request,'posts/main.html', {'posts': posts})

def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'posts/show.html', {'post':post})