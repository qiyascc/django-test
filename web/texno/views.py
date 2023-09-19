from django.shortcuts import render
from . import models
def index(request):
    projects = models.Project.objects.filter(is_active=True)
    context = {
        'projects': projects
    }
    return render(request, 'texno/index.html', context=context)
