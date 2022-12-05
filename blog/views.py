from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CommentForm
from .models import Post, Comment


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context


def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post = post.post
    if request.user.is_authenticated and request.user == post.author:
        post.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/review/')


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']

    template_name = 'blog/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

# def index(request):
#    posts = Post.objects.all().order_by('-pk')

#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts': posts,
#        }
#    )

# def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)

#    return render(
#        request,
#        'blog/single_post_page.html',
#        {
#            'post': post,
#        }
#    )
