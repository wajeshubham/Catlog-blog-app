from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils import timezone
from users.form import CommentForm
from .models import Post, Comment


# Create your views here.
@login_required
def home(request, **kwargs):
    context = {'posts': Post.objects.all(), }
    return render(request, 'myApp/home.html', context)


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'myApp/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3


class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'myApp/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')




class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        kwargs['comments']=Comment.objects.all().order_by('-date')
        return super(PostDetailView,self).get_context_data(**kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ProfilePostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'users/profile.html'
    success_url = 'user_post_profile'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2

    def get_queryset(self,**kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


@login_required
def likes(request, **kwargs):
    if request.method == 'POST':
        post_liked = get_object_or_404(Post, pk=kwargs.get('pk'))
        if post_liked.likes.filter(pk=request.user.pk).exists():
            post_liked.likes.remove(request.user)
        else:
            post_liked.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required
def comment(request, **kwargs):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        c_form = CommentForm(request.POST,instance=request.user)
        if c_form.is_valid():
            c_form.save()
            content = c_form.cleaned_data.get('content')
            created_comment = Comment.objects.create(user=request.user, content=content, post=post)
            created_comment.save()

            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        c_form = CommentForm(instance=request.user)

    context = {'c_form': c_form,
               'comments' : Comment.objects.filter(post=post).order_by('-date'),
               'user':request.user,
               'post':post
                }
    return render(request, 'users/comment_list.html', context)



@login_required
def comment_likes(request, **kwargs):
    if request.method == 'POST':
        comment_liked = get_object_or_404(Comment, pk=kwargs.get('pk'))
        if comment_liked.comment_likes.filter(pk=request.user.pk).exists():
            comment_liked.comment_likes.remove(request.user)
        else:
            comment_liked.comment_likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def about(request):
    return render(request,"myApp/about.html")