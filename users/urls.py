from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'), #added new path for add.html
    path('processadd', views.processadd, name='processadd'),
    path('<int:profile_id>/detail/', views.detail, name='detail'), #link to show the full detail of profile when clicked
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)