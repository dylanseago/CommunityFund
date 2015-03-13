from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from communityfund.apps.home.models import Project, Community
from communityfund.apps.home.forms import FundingForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'home/index.html', {
        'projects': Project.objects.all(),
        'communities': Community.objects.all(),
    })


def about(request):
    return render(request, 'home/about.html')


def projects(request):
    return render(request, 'home/projects.html', {
        'projects': Project.objects.all()
    })


def communities(request):
    return render(request, 'home/communities.html', {
        'communities': Community.objects.all()
    })


@login_required
def create_community(request):
    #TODO
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        return render(request, 'home/create_community.html', {
            'community_form': {},
        })


@login_required
def create_project(request):
    return HttpResponseRedirect('/')


def user(request, user_id):
    return render(request, 'home/user.html', {
        'user_profile': get_object_or_404(User, pk=user_id),
    })


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    user_contribution = None
    if request.method == 'POST':
        form = FundingForm(request.user, project, request.POST)
        if form.is_valid():
            funding = form.save()
            user_contribution = funding.amount
    else:
        form = FundingForm(request.user, project)
        fundings = project.fundings.filter(user__id=request.user.id)
        if len(fundings) != 0:
            user_contribution = fundings[0].amount
    return render(request, 'home/project.html', {
        'project': project,
        'forms': {
            'funding': form
        },
        'user_contribution': user_contribution
    })


def community(request, community_id):
    return render(request, 'home/community.html', {
        'community': get_object_or_404(Community, pk=community_id),
    })