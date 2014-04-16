from tornado.web import URLSpec as r
from {{ cookiecutter.project }}.auth.handlers import LoginHandler, LogoutHandler

urls = (
    # {{ cookiecutter.project }}.auth
    r(r'/auth/login/', LoginHandler, name='login'),
    r(r'/auth/logout/', LogoutHandler, name='logout'),
)
