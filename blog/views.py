from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        return context


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post = post.delete()
    if request.user.is_authenticated and request.user == Post.author:
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
