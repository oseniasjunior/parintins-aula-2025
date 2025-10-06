from rest_framework import serializers, exceptions

import cruds
from cruds import models, actions, mixins


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaritalStatus
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class ProductGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Supplier


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'



#
#
# class StateSerializer(mixins.StateSerializerMixin, serializers.Serializer):
#     name = serializers.CharField(max_length=64, required=True)
#     abbreviation = serializers.CharField(max_length=2, required=True)
#     #
#     # def validate(self, data):
#     #     result = actions.StateAction.validate_uppercase(data)
#     #     return super().validate(result)
#
#     def create(self, validated_data: dict):
#         return models.State.objects.create(**validated_data)
#
#     def update(self, instance: dict, validated_data: dict):
#         for k, v in validated_data.items():
#             setattr(instance, k, v)
#
#         instance.save()
#         return instance


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'
