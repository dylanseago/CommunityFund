from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET",])
def echo(request):
	html = "<html><body>echo_msg: %s.</body></html>" % request.GET.get('q', '')
	return HttpResponse(html)

