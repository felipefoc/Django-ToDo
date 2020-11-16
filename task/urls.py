from django.urls import path
from . import views


urlpatterns = [
    path('task/', views.add_task, name='add_task'),
    path('remove_task/<pk>', views.remove_task, name='remove_task'),

    ]   