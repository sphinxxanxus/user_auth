"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
