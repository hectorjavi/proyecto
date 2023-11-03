from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .. import models
from . import serializers


class ReserveViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "get", "put", "patch", "delete"]
    pagination_class = serializers.ReservePagination
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_fields = [
        "laboratory__id",
    ]
    ordering_fields = [
        "created",
        "modified",
    ]
    ordering = ["-created"]

    def get_queryset(self, **kwargs):
        return models.Reserve.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.ReserveCreateSerializer
        if self.action == "update":
            return serializers.ReserveUpdateSerializer
        if self.action == "partial_update":
            return serializers.ReservePartialUpdateSerializer

        return serializers.ReserveResponseSerializer
