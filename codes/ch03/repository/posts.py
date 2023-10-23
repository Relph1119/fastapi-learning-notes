from model.posts import Post

posts = dict()


class PostRepository:
    def __init__(self):
        pass

    def insert_post(self, post: Post):
        posts[post.id] = post

    def query_posts(self):
        return list(posts.values())
