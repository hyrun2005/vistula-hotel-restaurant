from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.login_in, name='login_in')
]
