# This import is very weird
import tornado, tornado.auth

import {{ cookiecutter.app }}.handler
from {{ cookiecutter.app }}.auth.models import User


class LoginHandler({{ cookiecutter.app }}.handler.Handler,
                   tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("openid.mode", None):
            user_data = yield self.get_authenticated_user()
            if not user_data:
                raise tornado.web.HTTPError(500, "Google auth failed")
            try:
                user = yield User.objects.get(email=user_data['email'])
            except:
                user = None
            if not user:
                # Auto-create first author
                any_author = yield User.objects.count()
                if not any_author:
                    user = User(name=user_data['name'],
                                email=user_data['email'])
                    yield user.save()
                else:
                    self.redirect("/")
                    return
            self.set_secure_cookie("user", str(user._id))
            self.redirect(self.get_argument("next", "/"))
        else:
            self.authenticate_redirect()


class LogoutHandler({{ cookiecutter.app }}.handler.Handler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))
