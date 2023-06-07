from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


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
    context = {"project": project}
    return render(request, "projects/detail.html", context)


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create.html", context)
