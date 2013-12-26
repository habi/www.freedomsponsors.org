import json
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from core.models import Project
from core.services import stats_services
from core.signals import project_edited
from core.views import template_folder

__author__ = 'tony'


def view(request, project_id):
    project = Project.objects.get(pk=project_id)
    stats = stats_services.project_stats(project)
    return render_to_response('core2/project.html',
                              {'project': project,
                               'stats': stats,
                               'tags': json.dumps([t.name for t in project.get_tags()])},
                              context_instance=RequestContext(request))


def edit_form(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render_to_response('core2/project_edit.html',
                              {'project': project},
                              context_instance=RequestContext(request))


def edit(request):
    project_id = int(request.POST.get('id'))
    project = Project.objects.get(pk=project_id)
    old_project_json = project.to_json()
    if 'image3x1' in request.FILES and request.FILES['image3x1']:
        project.image3x1 = request.FILES['image3x1']
    project.description = request.POST.get('description')
    project.save()
    project_edited.send(
        sender=None,
        user=request.user,
        project=project,
        old_json=old_project_json)
    return redirect('core.views.project_views.view', project_id=project.id)


def list(request):
    projects = Project.objects.all()
    projects = projects.order_by('name')
    return render_to_response(template_folder(request) + 'project_list.html',
        {'projects':projects},
        context_instance = RequestContext(request))