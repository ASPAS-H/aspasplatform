from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.showIndex),
    path('consults', views.view_consults),
    path('map', views.showMap),
    path('register', views.showRegister),
    path('status', views.showStatus),
    path('new/consult', views.newConsult),
    path('new/consult/', views.newConsult),
    path('consult/<int:consult_id>', views.view_consult)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)