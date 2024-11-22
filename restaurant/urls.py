from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainPageRes, name='restaurantHomePage'),
    path('menu/', views.menu, name='res_menu')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
