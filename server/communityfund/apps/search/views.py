from django.db.models import query
from django.template import Template, Context
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from communityfund.apps.home.models import Project, User, Community
from communityfund import placeholder
from django.db.models import Q

@require_http_methods(['GET'])
def echo(request):
    #html = "Search keyword: " + str(request.GET.get('q', '')) + "<br>"
    #project = Project.get_Project(name=request.GET.get('q', ''))
    #html += simple_textify(project, "<br>")
    return HttpResponse("")


@require_http_methods(['GET'])
def results(request):
    query = request.GET.get('q', '')
    db_query = Q(name__icontains=query) | Q(description__icontains=query)
    projects = Project.objects.all().filter(db_query)
    communities = Community.objects.all().filter(db_query)
    return render(request, 'search/results.html', {
        'projects': projects,
        'communities': communities,
        'search_query': query
    })


def simple_textify(obj, seperate_str=None):
    temp = [seperate_str]
    if type(obj) == query.QuerySet:
        for items in obj:
            temp.append(items.__str__())
            temp.append(seperate_str)
    else:
        temp.append(obj.__str__())
        temp.append(seperate_str)
    if seperate_str is None:
        return str(temp)
    else:
        return str(temp) + seperate_str

