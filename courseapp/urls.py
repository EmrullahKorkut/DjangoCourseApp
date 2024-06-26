from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurslar/', include('courses.urls')),
    path('', include('pages.urls')),
]
