from utils.base import SiteRequestHandler

class Home(SiteRequestHandler):
    def __init__(self):
        super(Home, self).__init__()

    def initialize(self, request):
        #BasePublicPage.initialize(self, request)
        super(Home, self).initialize(request)

    # def HEAD(self,page=1):
    #     if self.blog.allow_pingback:
    #         self.response.headers['X-Pingback']="%s/rpc"%str(self.blog.baseurl)
    def GET(self, page = 1):
        postid=self.param('p')
        context = { }
        self.render('trans/index.html', context)

    # def POST(self):
    #     postid=self.param('p')
    #     if postid:
    #         try:
    #             postid=int(postid)
    #             #doRequestPostHandle(self,SinglePost(),postid=postid)  #singlepost.get(postid=postid)
    #             self.response = SinglePost(self.request, postid=postid)
    #         except:
    #             self.error(404)

class Chapter(SiteRequestHandler):
    def GET(self, book = '', idx = 1):
        context = {'book': book,
                   'idx': idx}
        self.render('trans/chapter.html', context)
