from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name= 'blog_list'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_post, name= 'add_post'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name= 'delete_post'),

]