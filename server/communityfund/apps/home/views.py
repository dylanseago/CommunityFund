from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from communityfund.apps.home.models import Placeholder


def index(request):
    # TODO: Replace placeholders with database values
    return render(request, 'home/index.html', {
        'projects': [Placeholder.project(i) for i in range(10)],
        'communities': [Placeholder.community(i) for i in range(10)],
    })


def projects(request):
    # TODO: Replace placeholders with database values
    return render(request, 'home/projects.html', {
        'projects': [Placeholder.project(i) for i in range(15)]
    })


def communities(request):
    # TODO: Replace placeholders with database values
    return render(request, 'home/communities.html', {
        'communities': [Placeholder.community(i) for i in range(15)]
    })


@login_required
def profile(request):
    return user(request, 0)


def community(request, community_id):
    # TODO: Replace placeholder with database value
    return render(request, 'home/community.html', {
        'community': Placeholder.community(community_id),
    })


def project(request, project_id):
    # TODO: Replace placeholder with database value
    return render(request, 'home/project.html', {
        'project': Placeholder.project(project_id),
    })


def user(request, user_id):
    # TODO: Replace placeholder with database value
    return render(request, 'home/user.html', {
        'user': Placeholder.user(user_id),
    })