from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('register/', views.create),
    path('login', views.login)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)