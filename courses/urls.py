from django.urls import path
from courses import views

urlpatterns = [
    path('', views.kurslar),
    path('kurslar', views.kurslar),
    path('liste', views.kurs_liste),
    path('<kurs_adi>', views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryID),
    path('kategori/<str:category_name>', views.getCoursesByCategory, name='course_by_category'),

]
