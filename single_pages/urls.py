from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('pricing', views.pricing),
    path('sign_up', views.sign_up),
    path('community', views.community),
    path('features', views.features),
    path('example', views.example),
]
