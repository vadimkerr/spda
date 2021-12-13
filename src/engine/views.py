# Create your views here.

from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "engine/index.html"


class ChangeLanguageView(TemplateView):
    template_name = "engine/change_language.html"
