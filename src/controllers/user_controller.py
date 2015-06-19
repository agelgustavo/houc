
class UserController(object):

    def __init__(self, request, response):
        self.request = request
        self.response = response

    def get(self):
        print "get user"