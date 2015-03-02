from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from search.models import Project, User

@require_http_methods(["GET",])
def echo(request):
	#project=set_Project(pID="0", initiator="0", name="test", goal="test", description="t", timeToFund="10:00:00")
	#project=get_Project(project.objects.values('initiator'), project.objects.values('name'))
	#html = "<html><body>echo_msg: %s.</body></html>" % request.GET.get('q', '')
	user=User.get_User(uID=0)
	html=user.__str__()
	if (User.update_User(user, 1)):
		pass
	if (user.update_User(1)):
		pass	
	return HttpResponse(html)




