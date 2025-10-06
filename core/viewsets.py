from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models
from core import serializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    @action(detail=True, methods=['PATCH'])
    def calc_bonus(self, request, *args, **kwargs):
        bonus_percentage = request.data.get('bonus_percentage', 0)
        employee = self.get_object()
        employee.salary += employee.salary * bonus_percentage / 100
        employee.save()
        return Response(status=status.HTTP_200_OK, data={'detail': 'Calculado o bônus do funcionário'})
