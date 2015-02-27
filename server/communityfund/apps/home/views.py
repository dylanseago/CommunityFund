from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	#index_html = loader.get_template('index.html')
	#return HttpResponse(index_html.render(...))

	# simple html
	return render_to_response('index.html')
