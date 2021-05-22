from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('error', views.error),
    path('register', views.selectRegisterPage)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)