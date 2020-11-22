from django.urls import path
from . import views


urlpatterns = [
    path('youtube/', views.download_video, name='youtube'),
    path('youtube/download/', views.download, name='download'),
    path('youtube/download_api/<int:id>', views.download_api, name='download_api'),
    path('youtube/download_only_audio/', views.download_only_audio, name='download_only_audio'),
    path('youtube/download/delete', views.delete_file, name='delete'),
    ]   