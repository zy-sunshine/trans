from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
    c = Context({'person': {'first_name': 'Glenn', 'last_name': 'Zhang'}})
    return HttpResponse(t.render(c))
