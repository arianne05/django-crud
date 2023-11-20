from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'), #added new path for add.html for the created add class in views.py
    path('search', views.search, name='search'), #added new path for search
    path('processadd', views.processadd, name='processadd'),
    path('<int:profile_id>/detail/', views.detail, name='detail'),
    path('<int:profile_id>/delete/', views.delete, name='delete'),
    path('<int:profile_id>/edit/', views.edit, name='edit'),
    path('<int:profile_id>/processedit/', views.processedit, name='processedit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)