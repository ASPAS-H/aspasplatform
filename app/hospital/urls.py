from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Create your urls here.

urlpatterns = [
    path('', views.showIndex),
    path('info', views.showInfo),
    path('test',views.showTest),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)