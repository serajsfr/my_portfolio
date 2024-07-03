from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Skill
from .forms import ProjectForm

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, "pages/home.html", {'projects': projects, 'skills': skills})

def edit_projects(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, "pages/edit_projects.html", {'form': form})
