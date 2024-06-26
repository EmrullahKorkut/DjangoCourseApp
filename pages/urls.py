from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home),
    path('iletisim', views.iletisim),
    path('anasayfa', views.home),
    path('hakkimizda', views.hakkimizda),
    
]
