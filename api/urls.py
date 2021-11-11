from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.getRoutes.as_view()),
    # path('projects/', views.getProjects.as_view()),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
