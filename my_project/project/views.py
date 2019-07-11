from django.conf import settings
from django.shortcuts import render

from .forms import ProjectForm
from .models import Project


# Create your views here.
def my_project_create(request):
    image_link = request.FILES.get("image")
    image_link = settings.BASE_DIR + "\\" + str(image_link)
    if request.method == "POST":
        my_form = ProjectForm(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
            my_form = ProjectForm()
    else:
        my_form = ProjectForm()



    context = {
        "form": my_form,
    }

    return render(request, "project_create.html", context)


def my_project_view(request):
    projects = []
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "project_view.html", context)
