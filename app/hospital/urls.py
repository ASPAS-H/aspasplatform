from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Create your urls here.

urlpatterns = [
    path('', views.showIndex),
    path('/info/<int:id>', views.showInfo),
    path('/test',views.showTest),
    path('/consults', views.showConsults),    
    path('/patient/<int:id>/<int:consult>', views.showPatientDetails),
    path('/manage',views.showManage),
    path('/videocall',views.showVideocall),
    path('/payment',views.showPayment),
    path('/consultdata',views.showConsultData),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)