from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index),
    path('consultas', views.viewConsults),
    path('info-solicitacoes/<int:id>', views.infoSolicitationView),
    path('info-datas/<int:id>', views.infoDatesView),
    path('solicitacoes', views.solicitationView),
    path('register', views.registerViewInterpreter),
    path('pagamento', views.paymentView),
    path('aceitar/<int:id>', views.updateAcceptConsult),
    path('desmarcar/<int:id>', views.markOffConsult),
    path('rejeitar/<int:id>', views.addRejectConsult)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

