from . import views
from django.urls import path, include

urlpatterns = [
    path('/', views.mainPage(), name='homePage')
]
