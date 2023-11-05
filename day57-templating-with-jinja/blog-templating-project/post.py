import json


class Post:
    def __init__(self):
        with open("../blog-data.json") as file:
            self.data = json.load(file)["posts"]
            self.post = None

    def find_post(self, post_id):
        for post in self.data:
            if post["id"] == int(post_id):
                self.post = post
        return self.post
