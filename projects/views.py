from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .form import Project_Form
from django.views import View
# Create your views here.


class projects(View):
    def get(self, request):
        search_querry = ''
        if request.GET.get('search_querry'):
            search_querry = request.GET.get('search_querry')
        print(search_querry)
        projcList = Project.objects.filter(title__contains=search_querry)
        content = {'projcList': projcList}
        return render(request, 'projects/projects.html', content)


class project(View):
    def get(self, request, pk):
        projectObj = Project.objects.get(id=pk)
        return render(request, 'projects/project.html', {'projectObj': projectObj})


class create_project(LoginRequiredMixin, View):
    def get(self, request):
        form = Project_Form()
        context = {'form': form}
        return render(request, "projects/projectform.html", context)

    def post(self, request):
        form = Project_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')


class update_project(LoginRequiredMixin, View):
    def get(self, request, pk):
        _project = Project.objects.get(id=pk)
        form = Project_Form(instance=_project)
        context = {'form': form}
        return render(request, "projects/projectform.html", context)

    def post(self, request, pk):
        _project = Project.objects.get(id=pk)
        form = Project_Form(request.POST, request.FILES, instance=_project)
        if form.is_valid():
            form.save()
            return redirect('projects')


class delete_project(LoginRequiredMixin, View):
    def get(self, request, pk):
        _project = Project.objects.get(id=pk)
        form = Project_Form(instance=_project)
        context = {'form': form}
        return render(request, "projects/delete_projectform.html", context)

    def post(self, request, pk):
        _project = Project.objects.get(id=pk)
        _project.delete()
        return redirect('projects')
