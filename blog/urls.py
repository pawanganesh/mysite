from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('create', views.create_blog_post, name="create"),
    path('<slug>/', views.detail_blog_view, name="detail"),
    path('<slug>/edit', views.edit_blog_view, name="edit"),
    
]