from django.db.models import query
from django.template import Template, Context
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from communityfund.apps.search.models import Project, User
from communityfund import placeholder


@require_http_methods(["GET"])
def echo(request):
    html = "Search keyword: " + str(request.GET.get('q', '')) + "<br>"
    project = Project.get_Project(name=request.GET.get('q', ''))
    html += simple_textify(project, "<br>")
    return HttpResponse(html)


@require_http_methods(["GET"])
def results(request):
    #search_projects = Project.get_Project(name=request.GET.get('q', ''))
    return render(request, 'search/results.html', {
        "projects": [placeholder.project(i) for i in range(10)],
        'communities': [placeholder.community(i) for i in range(10)]
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
    if seperate_str == None:
        return str(temp)
    else:
        return str(temp) + seperate_str

