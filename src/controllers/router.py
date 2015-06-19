import webapp2
import importlib

class UrlRouter(webapp2.RequestHandler):
    def dispatch(self):
        method = getattr(self._get_obj(), self.request.method.lower())
        method()

    def _get_obj(self):
        try:
            path = self.request.path
            req = self.request
            resp = self.response
            entire_path = path.split('/')
            if entire_path[3] == '':
                clazz = entire_path[2].title()
            else:
                clazz = entire_path[3]
            module = entire_path[2] + '_controller'
            m = importlib.import_module('src.controllers.' + module)
            clazz_name = clazz.split('?')[0]
            clazz = getattr(m, clazz_name + "Controller")
            return clazz(req, resp)
        except Exception as e:
            raise e

app = webapp2.WSGIApplication([
    ('/s/.*', UrlRouter),
], debug=True)
