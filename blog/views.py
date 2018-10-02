from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Blog, Category
from blog.forms import BlogForm,LoginForm
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Blog.objects.order_by('-date_ajout')
    paginator = Paginator(posts, 4) # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts':posts}
    return render(request,'blog/home.html',context)

def view_post(request,blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    context ={'post':post}
    return render(request,'blog/view_post.html',context)

def view_category(request,slug):
    categories = get_object_or_404(Category, slug=slug)
    context ={
    'categories': categories,
    'posts':posts
    }
    cat = Blog.objects.filter(category=category)[:5]
    return render(request,'blog/view_category.html',context)

def base(request):
    return render(request,'blog/base.html')

def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'post a ete ajoute avec succes :')
            return redirect('home')
    else:
        form = BlogForm()
        context ={'form':form}
    return render (request,'blog/add_post.html',context)


def edit_post(request,blog_id):
    if request.method == 'POST':
        current_post = Blog.objects.get(pk=blog_id)
        form = BlogForm(request.POST or None,instance=current_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'post a ete edite avec succes :')
            return redirect('home')
        else :
            messages.success(request, 'erreur d\'edition post:')
            return render(request,'blog/edit_post.html')
    else:
        get_post = Blog.objects.get(pk=blog_id)
        context ={'get_post':get_post}
        return render (request,'blog/edit_post.html',context)


def delete(request,blog_id):
    if request.method == 'POST':
        current_post = Blog.objects.get(pk=blog_id)
        current_post.delete()
        return redirect('home')
    else:
        return redirect('home')


def login(request):
    form = LoginForm(request.POST)
    context={'form':form}
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    return render(request,'blog/login.html',context)

def search(request):
    query = request.GET.get('query')
    if not query:
        blog = get_object_or_404()
    else:
        blog = Blog.objects.filter(title__icontains=query)
    if not blog.exists():
        blog = Blog.objects.filter(category__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'blog': blog,
        'title': title
    }
    return render(request, 'blog/search.html', context)
# def view_post(request, slug):
#    return render_to_response('view_post.html', {
#        'post': get_object_or_404(Blog, slug=slug)
#    })
#
# def view_category(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    return render_to_response('view_category.html', {
#        'category': category,
#        'posts': Blog.objects.filter(category=category)[:5]
#    })
