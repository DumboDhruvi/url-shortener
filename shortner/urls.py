from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the homepage (shorten URL form)
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),  # URL for redirecting shortened URLs
]
