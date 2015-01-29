import json
import falcon
from blog_models import *

app = application = falcon.API()

class PostsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp, post_id):
        post = WpPosts.get(WpPosts.id == post_id)
        user = WpUsers.get(WpUsers.id == post.post_author)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"post_content": post.post_content,
                                "author": user.display_name})


class AllPostsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp):
        result = []
        blog_posts = WpPosts.select().where(WpPosts.post_status == "publish")
        for post in blog_posts:
            result.append({"posts": post.post_content})

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result)


posts = PostsResource()
allPosts = AllPostsResource()

app.add_route('/posts/{post_id}', posts)
app.add_route('/all/posts', allPosts)