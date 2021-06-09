from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Create your urls here.

urlpatterns = [
<<<<<<< HEAD
    path('hospital', views.hospital_index),
    path('informacoes', views.hospital_informacoes),
    path('consultas', views.hospital_consultas),    
=======
    path('', views.showIndex),
    path('info', views.showInfo),
    path('test',views.showTest),
>>>>>>> 5bbf7e0380d97804437e603abc406541ad6bd345

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)