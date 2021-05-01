from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index),
    path('consults/', views.viewConsults),
    path('info/', views.infoView),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

