from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    form = PostForm()
    return render(request, 'blog/home.html', {'form': form})

def post(request):
    form = PostForm()
    if request.method == "POST":
        posts = PostForm(request.POST)
        if posts.is_valid():
            userObj = posts.cleaned_data
            name = userObj['name']
            text = userObj['text']
            Post.objects.create(name = name, text = text)
            return redirect('/success')
        else:
            return render(request, 'blog/home.html', {'form': form})
    else:
        return render(request, 'blog/home.html', {'form':form})

def success(request):
    return render(request, 'blog/success.html')