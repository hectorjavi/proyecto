from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .. import models
from . import serializers


class LaboratoryViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "get", "put", "patch", "delete"]
    pagination_class = serializers.LaboratoryPagination
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    search_fields = ["name"]
    ordering_fields = [
        "created",
        "modified",
        "name",
    ]
    ordering = ["name"]

    def get_queryset(self, **kwargs):
        return models.Laboratory.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.LaboratoryCreateSerializer
        if self.action == "update":
            return serializers.LaboratoryUpdateSerializer
        if self.action == "partial_update":
            return serializers.LaboratoryPartialUpdateSerializer

        return serializers.LaboratoryResponseSerializer
