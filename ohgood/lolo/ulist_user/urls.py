from django.urls import path
from .views import *
urlpatterns = [
    path('', profile_list, name='profiles'),
    path('<uuid:pk>/', profile_detail, name='profiles-detail'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register_view, name='register'),
    path('user_account/', user_account, name='user_account'),
    path('edit_account/', edit_account, name='edit_account'),  
    path('create_skill/', create_skill, name='create_skill'),  
    path('skill/edit/<uuid:pk>/', update_skill, name='update_skill'),
    path('skill/delete/<uuid:pk>/', delete_skill, name='delete_skill'),   # Assuming delete_skill is a function in views.py
    path('inbox/', inbox, name='inbox'),   # Assuming inbox is a function in views.py
    path('message/<uuid:pk>/', view_message, name='message'), # Assuming inbox is a function in views
    path('create-message/<uuid:pk>/', createMessage, name='create-message'),
] 

