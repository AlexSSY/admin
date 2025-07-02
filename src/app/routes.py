from starlette.routing import Route

from . import views


routes = [
    Route("/", views.home, methods=["GET"], name="home"),
]
