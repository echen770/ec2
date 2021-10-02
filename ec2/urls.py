from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path(
        "css/styles.css",
        TemplateView.as_view(template_name="style.css", content_type="text/css"),
    ),
]
