from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):
    item = Project.objects.filter(owner=request.user)
    context = {
        "projects": item,
    }
    return render(request, "projects/list.html", context)


@login_required
def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {
        "project": project
    }
    return render(request, "projects/detail.html", context)
