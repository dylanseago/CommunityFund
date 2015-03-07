from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from communityfund import placeholder
from django.http import HttpResponseRedirect


def index(request):
    # TODO: Replace placeholders with database values
    return render(request, 'home/index.html', {
        'projects': [placeholder.project(i) for i in range(10)],
        'communities': [placeholder.community(i) for i in range(10)],
    })


def about(request):
    return render(request, 'home/about.html')


def projects(request):
    # TODO: Replace placeholders with database values
    return render(request, 'home/projects.html', {
        'projects': [placeholder.project(i) for i in range(15)]
    })


def communities(request):
    # TODO: Replace placeholders with database values
    return render(request, 'home/communities.html', {
        'communities': [placeholder.community(i) for i in range(15)]
    })


@login_required
def create_community(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        form = {}
        return render(request, 'home/create_community.html', {
            'community_form': form,
        })


@login_required
def create_project(request):
    return HttpResponseRedirect('/')


def user(request, user_id):
    # TODO: Replace placeholder with database value
    return render(request, 'home/user.html', {
        'user_profile': placeholder.user(user_id),
    })


def project(request, project_id):
    # TODO: Replace placeholder with database value
    return render(request, 'home/project.html', {
        'project': placeholder.project(project_id),
    })


def community(request, community_id):
    # TODO: Replace placeholder with database value
    return render(request, 'home/community.html', {
        'community': placeholder.community(community_id),
    })