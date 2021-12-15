from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from engine.models import Application


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application

    def get_queryset(self):
        return self.request.user.applications.all()


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ["title", "link", "price", "start_date", "quarter", "justification"]
    success_url = reverse_lazy("engine:list")
    template_name_suffix = "_create_form"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields["price"].required = False
        form.fields["start_date"].required = False

        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ["title", "link", "price", "start_date", "quarter", "justification"]
    success_url = reverse_lazy("engine:list")
    template_name_suffix = "_update_form"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields["price"].required = False
        form.fields["start_date"].required = False

        return form


class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy("engine:list")


class ChangeLanguageView(TemplateView):
    template_name = "engine/change_language.html"
