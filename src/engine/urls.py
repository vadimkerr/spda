from django.urls import path

from .views import (
    ApplicationCreateView,
    ApplicationDeleteView,
    ApplicationListView,
    ApplicationUpdateView,
)

app_name = "engine"


urlpatterns = [
    path("list/", ApplicationListView.as_view(), name="list"),
    path("create/", ApplicationCreateView.as_view(), name="create"),
    path("<pk>/delete/", ApplicationDeleteView.as_view(), name="delete"),
    path("<pk>/update/", ApplicationUpdateView.as_view(), name="update"),
]
