from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', views.Profiles.as_view(), name='profiles'),
    path('profile/<str:pk>/', views.UserProfile.as_view(), name='UserProfile'),
    path('login/', views.LoginPage.as_view(), name='LoginPage'),
    path('logout/', views.loginoutUser.as_view(), name='loginoutUser'),
    path('register/', views.registerUser.as_view(), name='register'),
    path('account/', views.userAccount.as_view(), name='account'),
]
