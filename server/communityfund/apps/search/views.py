from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from search.models import Project, User

@require_http_methods(["GET",])
def echo(request):
	#project=set_Project(pID="0", initiator="0", name="test", goal="test", description="t", timeToFund="10:00:00")
	#project=get_Project(project.objects.values('initiator'), project.objects.values('name'))
	#html = "<html><body>echo_msg: %s.</body></html>" % request.GET.get('q', '')
	user=User.objects.get(uID=0)
	html=user.__str__()
	return HttpResponse(html)

def get_Project(initiator=None, name=None):
	if (not initiator and not name):
		return None
	project=[]
	try:
		if (name):
			project=Project.objects.get(name=name)
		else:
			project=Project.objects.get(initiator=initiator)
	except Project.DoesNotExist:
		return None
	return project

def set_Project(pID, initiator, name, goal, description, timeToFund):
	project=Project.create(pID=pID, initiator=initiator, name=name, goal=goal, description=description, timeToFund=timeToFund)
	return project

def update_Project(pObj, pID, initiator, name, goal, description, timeToFund):
	pObj.pID=pID
	pObj.initiator=initiator
	pObj.name=name
	pObj.goal=goal
	pObj.description=description
	pObj.timeToFund=timeToFund
	try:
		pObj.save()
	except:
		return None
	return pObj



