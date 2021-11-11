from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProjectSerializer
from projects.models import Project

from api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'GET': '/api/projects/id/vote'},
        {'POST': '/api/users/token/refresh'},
        {'POST': '/api/users/token'},
    ]
    return Response(routes)


class getRoutes(APIView):
    def get(self, request):
        routes = [
            {'GET': '/api/projects'},
            {'GET': '/api/projects/id'},
            {'GET': '/api/projects/id/vote'},
            {'POST': '/api/users/token/refresh'},
            {'POST': '/api/users/token'},
        ]
        return Response(routes)


# class getProjects(APIView):
#     # authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request):
#         project = Project.objects.all()
#         serializer = ProjectSerializer(project, many=True)
#         return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


class getProject(APIView):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
