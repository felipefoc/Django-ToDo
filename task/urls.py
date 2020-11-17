from django.urls import path
from . import views


urlpatterns = [
    path('task/', views.add_task, name='add_task'),
    path('complete_task/<pk>', views.complete_task, name='complete_task'),
    path('ended_tasks/', views.ended_tasks, name='ended_tasks'),
    path('remove_task/<pk>', views.remove_task, name='remove_task'),
    path('edit_task/<pk>', views.edit_task, name='edit_task'),
    ]   