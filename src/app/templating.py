from starlette.templating import Jinja2Templates

from . import settings, context_processors


templating = Jinja2Templates(settings.TEMPLATE_DIRS, context_processors=[context_processors.default])
