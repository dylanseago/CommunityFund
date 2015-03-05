from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


def index(request):
	#index_html = loader.get_template('index.html')
	#return HttpResponse(index_html.render(...))

	# simple html
	return render_to_response('index.html')


def projects(request):
    return render_to_response('projects.html')


def communities(request):
    return render_to_response('communities.html')


@login_required
def profile(request):
    return render_to_response('user.html')