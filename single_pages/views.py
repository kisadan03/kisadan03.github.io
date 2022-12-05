from django.shortcuts import render
from blog.models import Post


# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )


def pricing(request):
    return render(
        request,
        'single_pages/pricing.html'
    )


def sign_up(request):
    return render(
        request,
        'single_pages/sign_up.html'
    )


def community(request):
    recent_posts = Post.objects.order_by('-pk')[:5]
    return render(
        request,
        'single_pages/community.html',
        {
            'recent_posts': recent_posts,
        }
    )


def features(request):
    return render(
        request,
        'single_pages/features.html'
    )


def example(request):
    return render(
        request,
        'single_pages/example.html'
    )


def mypage(request):
    return render(
        request,
        'single_pages/mypage.html'
    )
