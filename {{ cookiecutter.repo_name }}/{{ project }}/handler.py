import tornado

from {{ cookiecutter.app }}.auth.models import User


class Handler(tornado.web.RequestHandler):
    def get_current_user(self):
        if self.get_secure_cookie("user"):
            return User.objects.get(id=self.get_secure_cookie("user"))

    def absolute_url(self, name, *args, **kwargs):
        rc = "http://" + self.settings['domain_name']
        if self.settings.get('debug') and self.settings.get('port') \
           and self.settings.get('port') != 80:
            rc += ':' + str(self.settings['port'])
        try:
            rc += self.reverse_url(name, *args, **kwargs)
        except:
            rc += name
        return rc
