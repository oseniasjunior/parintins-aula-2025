from pickle import FALSE

from rest_framework import viewsets
from rest_framework.decorators import action

from cruds import serializers, models, filters, tasks


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


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer

    def create(self, request, *args, **kwargs):
        instance = super().create(request, *args, **kwargs)
        tasks.create_state_file.apply_async([instance.data.get('id')], countdown=1)
        return instance
