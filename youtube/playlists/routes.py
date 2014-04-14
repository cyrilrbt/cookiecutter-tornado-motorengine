from tornado.web import URLSpec as r
from youtube.playlists.auth.handlers import LoginHandler, LogoutHandler

urls = (
    # youtube.playlists.auth
    r(r'/auth/login/', LoginHandler, name='login'),
    r(r'/auth/logout/', LogoutHandler, name='logout'),
)
