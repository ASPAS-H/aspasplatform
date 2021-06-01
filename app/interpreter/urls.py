from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index),
    path('consultas', views.viewConsults),
    path('info-solicitacoes/', views.infoSolicitationView), #path('info/<int:id>', views.infoView)
    path('info-datas', views.infoDatesView),
    path('solicitacoes', views.solicitationView),
    path('interpreter/register', views.registerViewInterpreter),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

