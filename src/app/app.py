from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from . import settings
from . import routes


app = Starlette(debug=settings.DEBUG, routes=routes.routes)
static = StaticFiles(directory=settings.STATIC_FILES_DIR)
app.mount("/static", static, name="static")
