from django.urls import path
from .views import project_list, project_detail, project_create, project_update, project_delete

urlpatterns = [
    path('', project_list, name='project'),
    path('<uuid:pk>/', project_detail, name='project_detail'),
    path('create/', project_create, name='project_create'),
    path('<uuid:pk>/update/', project_update, name='project_update'),
    path('<uuid:pk>/delete/', project_delete, name='project_delete'),
]
