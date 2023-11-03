from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()


router.register(r"reservations", viewsets.ReserveViewSet, basename="reservations")

urlpatterns = router.get_urls()
