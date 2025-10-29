from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models
from core import serializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    ordering_fields = '__all__'
    ordering = ('-salary',)
    
    @action(detail=True, methods=['PATCH'])
    def calc_bonus(self, request, *args, **kwargs):
        bonus_percentage = request.data.get('bonus_percentage', 0)
        employee = self.get_object()
        employee.salary += employee.salary * bonus_percentage / 100
        employee.save()
        return Response(status=status.HTTP_200_OK, data={'detail': 'Calculado o bônus do funcionário'})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.SaleItem.objects.all()
    serializer_class = serializers.SaleItemSerializer
