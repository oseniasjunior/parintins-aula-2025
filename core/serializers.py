from rest_framework import serializers
from core import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

    def validate(self, data):
        if not data.get('name', '').isupper():
            raise Exception('O campo nome tem que ser em maiscuculo')
        return data

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale
        fields = '__all__'


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SaleItem
        fields = '__all__'
