from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()


router.register(r"laboratories", viewsets.LaboratoryViewSet, basename="laboratories")

urlpatterns = router.get_urls()
