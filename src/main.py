from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import settings
import routes


app = Starlette(debug=settings.DEBUG, routes=routes.routes)
static = StaticFiles(directory=settings.STATIC_FILES_DIR)
templating = Jinja2Templates(settings.TEMPLATE_DIRS)
