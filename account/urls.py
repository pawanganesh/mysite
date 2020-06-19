from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('account/', views.account_view, name="account"),
    path('must_authenticate/', views.must_authenticate_view, name="must_authenticated"),
]