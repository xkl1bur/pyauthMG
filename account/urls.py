from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('signin', views.sign_in, name='signin'),
  path('callback', views.callback, name='callback'),
]