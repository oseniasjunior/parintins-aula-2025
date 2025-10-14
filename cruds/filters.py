from django_filters import filters, FilterSet
from cruds import models


class MaritalStatusFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.MaritalStatus
        fields = []
