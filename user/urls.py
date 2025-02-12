from django.urls import path, include
from user import views
from user.views import login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('logout/', views.logout_view, name='logout'),
    path('recommend_car/', views.recommend_car, name='recommend_car'),
]