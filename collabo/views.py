from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    project_list = Project.objects.order_by('-date')
    context = {'project_list': project_list}
    return render(request, 'collabo/project_list.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}
    return render(request, 'collabo/project_detail.html',context)