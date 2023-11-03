from rest_framework import pagination, serializers
from rest_framework.response import Response

from ...person.api.serializers import PersonResponseSerializer
from ..models import Reserve


class ReservePagination(pagination.PageNumberPagination):
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


class ReserveResponseSerializer(serializers.ModelSerializer):
    person = PersonResponseSerializer(many=True)

    class Meta:
        model = Reserve
        fields = (
            "id",
            "date",
            "start_time",
            "end_time",
            "laboratory",
            "person",
            "created",
            "modified",
        )


class ReserveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = (
            "id",
            "date",
            "start_time",
            "end_time",
            "laboratory",
            "person",
            "created",
            "modified",
        )


class ReserveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = (
            "id",
            "date",
            "start_time",
            "end_time",
            "laboratory",
            "person",
            "created",
            "modified",
        )


class ReservePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = (
            "id",
            "date",
            "start_time",
            "end_time",
            "laboratory",
            "person",
            "created",
            "modified",
        )
