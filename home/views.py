from django.utils.translation import ugettext as _
# from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        output = _("Welcome to my site.")
        context = super(HomeView, self).get_context_data(**kwargs)
        context['greting'] = output
        context['description'] = _("Doing an awesome project. (str from views)")
        return context
