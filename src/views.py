from templating import templating


def home(request):
    return templating.TemplateResponse(request, "pages/home.html")
