from django.shortcuts import render


# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )


def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
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
    return render(
        request,
        'single_pages/community.html'
    )
