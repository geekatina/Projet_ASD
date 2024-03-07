from django.urls import path
from tasks import views



urlpatterns = [
    path('', views.task_list, name='task_list'),
    # path('add/', views.add_task, name='add_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('prioritize/', views.prioritize_tasks, name='prioritize_tasks'),
    path('prioritize_by_priority/', views.prioritize_tasks_by_priority, name='prioritize_tasks_by_priority'),
    
    
]
