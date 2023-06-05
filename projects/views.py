from django.shortcuts import render
from projects.models import Project


def project_list(request):
    item = Project.objects.all()
    context = {
        "projects": item,
    }
    return render(request, "projects/list.html", context)
