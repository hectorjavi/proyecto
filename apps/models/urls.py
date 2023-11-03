from django.urls import include, path

urlpatterns = [
    path("", include("apps.models.laboratory.urls")),
    path("", include("apps.models.reserve.urls")),
    path("", include("apps.models.person.urls")),
]
