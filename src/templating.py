from starlette.templating import Jinja2Templates

import settings


templating = Jinja2Templates(settings.TEMPLATE_DIRS)
