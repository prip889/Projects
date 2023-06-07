from django.urls import path
from .views import project_list, project_detail, project_create

urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", project_create, name="create_project"),
]
