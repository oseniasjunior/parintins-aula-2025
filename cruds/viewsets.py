from pickle import FALSE

from rest_framework import viewsets
from rest_framework.decorators import action

from cruds import serializers, models, filters


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer
    filterset_class = filters.MaritalStatusFilter
    ordering_fields = '__all__'
    ordering = ('id',)
    #
    # @action(detail=False, methods=['GET'])
    # def get_by_name(self, request, *args, **kwargs):
    #     name = request.query_params.get('name', '')
    #     self.queryset = models.MaritalStatus.objects.filter(name__icontains=name)
    #     return super().list(request, *args, **kwargs)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer


class SupplierGroupViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
