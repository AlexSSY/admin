from starlette.templating import Jinja2Templates

from . import settings, context_processors


templating = Jinja2Templates(settings.TEMPLATE_DIRS, context_processors=[context_processors.default])


def render_to_string(request, name, context={}):
    template = templating.get_template(name)
    ctx = context.copy()
    ctx.update({"request": request})
    return template.render(ctx)
