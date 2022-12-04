from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('q&a', views.about_me),
    path('pricing', views.pricing),
    path('sign_up', views.sign_up),
    path('community', views.community),
    path('features', views.features),
    path('example', views.example),
    path('view', views.exampleview),
]
