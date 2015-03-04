from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from search.models import Project, User

@require_http_methods(["GET",])
def echo(request):
	#project=set_Project(pID="0", initiator="0", name="test", goal="test", description="t", timeToFund="10:00:00")
	#project=get_Project(project.objects.values('initiator'), project.objects.values('name'))
	#html = "<html><body>echo_msg: %s.</body></html>" % request.GET.get('q', '')
	#user=User.get_User(uID=0)
	project=Project.get_Project(name=request.GET.get('q', ''))
	html=simple_textify(project, "<br>")
	user=User.get_User(uID=0)
	html+=simple_textify(user, "<br>")
	return HttpResponse(html)


def simple_textify(obj, seperate_str=None):
	temp = []
	if type(obj) == query.QuerySet:
		for items in obj:
			temp.append(items.__str__())
			temp.append(seperate_str)
	else:
		temp.append(obj.__str__())
		temp.append(seperate_str)
	return temp

