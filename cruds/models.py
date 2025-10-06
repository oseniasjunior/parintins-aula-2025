from django.db import models
from core import models as core_models
from cruds import managers


# Create your models here.


class ProductGroup(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)
    commission_percentage = models.DecimalField(null=False, decimal_places=2, max_digits=5)
    gain_percentage = models.DecimalField(null=False, decimal_places=2, max_digits=5)

    class Meta:
        db_table = 'product_group'
        managed = True


class Supplier(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False)
    legal_document = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'supplier'
        managed = True


class Product(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)
    cost_price = models.DecimalField(null=False, decimal_places=2, max_digits=16)
    sale_price = models.DecimalField(null=False, decimal_places=2, max_digits=16)
    product_group = models.ForeignKey(
        to='ProductGroup',
        null=False,
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
    )
    supplier = models.ForeignKey(
        to='Supplier',
        null=False,
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
    )
    objects = managers.ProductManager()

    class Meta:
        db_table = 'product'
        managed = True


class Department(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)

    class Meta:
        db_table = 'department'
        managed = True


class MaritalStatus(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)

    class Meta:
        db_table = 'marital_status'
        managed = True


class State(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False)
    abbreviation = models.CharField(max_length=2, null=False)

    class Meta:
        db_table = 'state'
        managed = True
        unique_together = ('name', 'abbreviation')

    def __str__(self):
        return f'{self.name} - {self.abbreviation}'


class City(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False)
    state = models.ForeignKey(
        to='State',
        null=False,
        on_delete=models.DO_NOTHING,
        db_column='id_state',
    )

    class Meta:
        db_table = 'city'
        managed = True
        unique_together = ('name', 'state')

    def __str__(self):
        return f'{self.name} - {self.state.name}'


class Zone(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)

    class Meta:
        db_table = 'zone'
        managed = True


class District(core_models.ModelBase):
    name = models.CharField(max_length=64, null=False)
    city = models.ForeignKey(
        to='City',
        null=False,
        on_delete=models.DO_NOTHING,
        db_column='id_city',
    )
    zone = models.ForeignKey(
        to='Zone',
        null=False,
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
    )

    class Meta:
        db_table = 'district'
        managed = True
        unique_together = ('name', 'city', 'zone')
