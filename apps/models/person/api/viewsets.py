from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .. import models
from . import serializers


class PersonViewSet(viewsets.ModelViewSet):
    http_method_names = ["post", "get", "put", "patch", "delete"]
    pagination_class = serializers.PersonPagination
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    search_fields = ["full_name", "dni"]
    ordering_fields = [
        "created",
        "modified",
        "full_name",
    ]
    ordering = ["-created"]

    def get_queryset(self, **kwargs):
        return models.Person.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PersonCreateSerializer
        if self.action == "update":
            return serializers.PersonUpdateSerializer
        if self.action == "partial_update":
            return serializers.PersonPartialUpdateSerializer

        return serializers.PersonResponseSerializer
