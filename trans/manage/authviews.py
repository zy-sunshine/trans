#from django import oldforms as forms
#from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response
#from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from trans.utils.base import SiteRequestHandler
from django.http import HttpResponseRedirect
# def register(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         data = request.POST.copy()
#         errors = form.get_validation_errors(data)
#         if not errors:
#             new_user = form.save()
#             return HttpResponseRedirect("/accounts/created/")
#     else:
#         data, errors = {}, {}

#     return render_to_response("registration/register.html", {
#         'form' : forms.FormWrapper(form, data, errors)
#     })
import logging
Log = logging.getLogger('django')
class Login(SiteRequestHandler):
    def POST(self):
        Log.info(self.request.uri)
        user = authenticate(username=self.param('username'), password=self.param('password'))
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # success
                self.redirect(self.referer)
        else:
            self.redirect(self.referer)

