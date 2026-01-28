from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [    
    # path('postlist/', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<str:slug>', views.post_edit, name='post_edit'),
    path('<str:slug>/delete', views.post_delete, name='post_delete'),
    path('<str:slug>', views.post_detail, name='post_detail'),
    
]