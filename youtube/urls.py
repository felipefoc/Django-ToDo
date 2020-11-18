from django.urls import path
from . import views


urlpatterns = [
    path('youtube/', views.download_video, name='youtube'),
    path('youtube/download/', views.download, name='download'),
    path('youtube/download/delete', views.delete_file, name='delete'),
    ]   