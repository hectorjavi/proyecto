from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()


router.register(r"persons", viewsets.PersonViewSet, basename="persons")

urlpatterns = router.get_urls()
