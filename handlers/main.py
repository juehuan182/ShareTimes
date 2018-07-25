import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    """
     Home page for user,photo feeds 主页----所关注的用户图片流
    """
    def get(self,*arg,**kwargs):
        self.render('index.html') #打开index.html网页


class ExploreHandler(tornado.web.RequestHandler):
    """
    Explore page,photo of other users 发现页-----发现或最近上传的图片页面
    """
    def get(self,*arg,**kwargs):
        self.render('explore.html')

class PostHandler(tornado.web.RequestHandler):
    """
    Single photo page and maybe  单个图片详情页面
    """
    def get(self,post_id):
        print(post_id)
        self.render('post.html',post_id = post_id)   #根据正则输入的内容，接收到，打开相应的图片