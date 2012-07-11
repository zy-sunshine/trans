import os
print os.path.dirname(os.path.abspath(__file__))

#From http://djangosnippets.org/snippets/2041/
class CallableViewClass(type):
    def __new__(cls, name, bases, dct):
        if 'HEAD' not in dct and 'GET' in dct:
            # XXX: this function could possibly be moved out
            # to the global namespace to save memory.
            def HEAD(self, request, *args, **kwargs):
                response = self.get(request, *args, **kwargs)
                response.content = u''
                return response
            dct['HEAD'] = HEAD

        dct['permitted_methods'] = []
        for method in ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'CONNECT', 'TRACE'):
            if hasattr(dct.get(method, None), '__call__'):
                dct['permitted_methods'].append(method)

        return type.__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        if args and isinstance(args[0], HttpRequest):
            instance = super(CallableViewClass, cls).__call__()
            return instance.__call__(*args, **kwargs)
        else:
            instance = super(CallableViewClass, cls).__call__(*args, **kwargs)
            return instance

class TemplateView(object):
    __metaclass__ = CallableViewClass

    def __call__(self, request, *args, **kwargs):
        if request.method in self.permitted_methods:
            handler = getattr(self, request.method)
            # XXX: Could possibly check if 'before' returns a response
            # and return that instead.
            #import pdb; pdb.set_trace()
            self.before(request, args, kwargs)
            if hasattr(self, 'initialize'):
                self.initialize(request)
            handler(*args, **kwargs)
            return self.response

        return HttpResponseNotAllowed(self.permitted_methods)

    def before(self, request, args, kwargs):
        """Override this method to add common functionality to all HTTP method handlers.

        args and kwargs are passed as regular arguments so you can add/remove arguments:
            def before(self, request, args, kwargs):
                kwargs['article'] = get_object_or_404(Article, id=kwargs.pop('article_id')
            def GET(self, request, article): # <== 'article' instead of 'article_id'
                ...
            def post(delf, request, article): # <== 'article' instead of 'article_id'
                ...
        """
        print 'before method'
        self.request = request
        self.response = HttpResponse()
        #self.response.headers = Setter(self.response)
        #self.response.out = Writer(self.response)
        #self.request.uri = get_absolute_path(request)
        #self.request.str_cookies = request.COOKIES
        #self.request.remote_addr = request.META['REMOTE_ADDR']
        #self.request.get_all = lambda x: request.REQUEST.getlist(x)
    def initialize(self, request):
        print 'initialize in TemplateView'

class HttpResponseNotAllowed:
    def __init__(self, method):
        pass
class HttpRequest:
    def __init__(self):
        self.method = "GET"
class HttpResponse:
    pass
class Test(TemplateView):
    def initialize(self, request):
        #TemplateView.initialize(self, request)
        super(Test, self).initialize(request)
        print 'initialize in Test'
    def GET(self):
        print 'Test GET method'
class Test2(Test):
    def GET(self):
        print 'Test2 GET method'

if __name__ == '__main__':
    request = HttpRequest()
    t = Test2(request)

