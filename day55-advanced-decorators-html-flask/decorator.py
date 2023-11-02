class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def authenticated_decorator(function):
    def wrapper(user):
        if user.is_logged_in:
            function(user)
    return wrapper


@authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Hailey")
new_user.is_logged_in = True
create_blog_post(new_user)
