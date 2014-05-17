from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext

def render_and_respond(request, template_name, context):
	t = loader.get_template(template_name)
	c = RequestContext(request, context)
	return HttpResponse(t.render(c))