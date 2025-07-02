from starlette.routing import Route

import views


routes = [
    Route("/", views.home, methods=["GET"], name="home"),
]
