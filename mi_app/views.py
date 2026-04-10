from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'mi_app/inicio.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'mi_app/detalle_post.html'
    
class PostCreateView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'mi_app/crear_post.html'

def home(request):
    return render(request, 'mi_app/home.html')


def inicio(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'mi_app/inicio.html', {'posts': posts})


def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'mi_app/detalle.html', {'post': post})


@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('mi_app:inicio')
    else:
        form = PostForm()

    return render(request, 'mi_app/crear_post.html', {'form': form})


@login_required
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.autor != request.user:
        return redirect('mi_app:inicio')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('mi_app:detalle_post', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'mi_app/editar_post.html', {'form': form, 'post': post})


@login_required
def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.autor != request.user:
        return redirect('mi_app:inicio')

    if request.method == 'POST':
        post.delete()
        return redirect('mi_app:inicio')

    return render(request, 'mi_app/eliminar_post.html', {'post': post})


def about(request):
    return render(request, 'mi_app/about.html')

def buscar(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Post.objects.filter(titulo__icontains=query)

    return render(request, 'mi_app/buscar.html', {
        'resultados': resultados,
        'query': query
    })