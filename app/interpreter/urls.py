from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index),
    path('consults', views.viewConsults),
    path('info', views.infoView),
    path('datas', views.datesView),
    path('solicitacoes', views.solicitationView),
    path('interpreter/register', views.registerViewInterpreter),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

