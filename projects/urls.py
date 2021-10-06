from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.projects.as_view(), name='projects'),
    path('project/<str:pk>/', views.project.as_view(), name='project_s'),
    path('create-project/', login_required(views.create_project.as_view()),
         name='create_project'),
    path('update-project/<str:pk>/',
         views.update_project.as_view(), name='update_project'),
    path('delete-project/<str:pk>/',
         views.delete_project.as_view(), name='delete_project')
]
