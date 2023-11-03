from rest_framework import pagination, serializers
from rest_framework.response import Response

from ..models import Laboratory


class LaboratoryPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 300

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "num_pages": self.page.paginator.num_pages,
                "page_number": self.page.number,
                "page_size": self.get_page_size(self.request),
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
            }
        )


class LaboratoryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            "id",
            "name",
            "sub_name",
            "descripcion",
            "created",
            "modified",
        )


class LaboratoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            "id",
            "name",
            "sub_name",
            "descripcion",
            "created",
            "modified",
        )


class LaboratoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            "id",
            "name",
            "sub_name",
            "descripcion",
            "created",
            "modified",
        )


class LaboratoryPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            "id",
            "name",
            "sub_name",
            "descripcion",
            "created",
            "modified",
        )
