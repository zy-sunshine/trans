from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
	# Method 1:
    #return render(request, 'trans/shortcut.tpl.html', {"foo": "bar"},
    #    content_type="application/xhtml+xml")
	# Method 2:
	return render_to_response('trans/shortcut.tpl.html',
                          {"foo": "bar"},
                          context_instance=RequestContext(request))
