from django.db import models

from core import managers


# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class GenderChoices:
    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')


class Branch(ModelBase):
    name = models.CharField(max_length=64, null=False, unique=True)
    district = models.ForeignKey(
        to='cruds.District',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_district',
    )

    class Meta:
        db_table = 'branch'
        managed = True


class Customer(ModelBase, GenderChoices):
    name = models.CharField(max_length=64, null=False)
    income = models.DecimalField(decimal_places=2, max_digits=16, null=False)
    gender = models.CharField(max_length=1, null=False, choices=GenderChoices.Gender.choices)
    district = models.ForeignKey(
        to='cruds.District',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_district',
    )
    marital_status = models.ForeignKey(
        to='cruds.MaritalStatus',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_marital_status',
    )
    objects = managers.CustomerManager()

    class Meta:
        db_table = 'customer'
        managed = True


class Employee(ModelBase, GenderChoices):
    name = models.CharField(max_length=64, null=False)
    salary = models.DecimalField(decimal_places=2, max_digits=16, null=False)
    admission_date = models.DateField(null=False)
    birth_date = models.DateField(null=False)
    gender = models.CharField(max_length=1, null=False, choices=GenderChoices.Gender.choices)
    department = models.ForeignKey(
        to='cruds.Department',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_department'
    )
    district = models.ForeignKey(
        to='cruds.District',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_district',
    )
    marital_status = models.ForeignKey(
        to='cruds.MaritalStatus',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_marital_status',
    )
    objects = managers.EmployeeManager()

    class Meta:
        db_table = 'employee'
        managed = True


class Sale(ModelBase):
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_customer',
    )
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_employee',
    )
    branch = models.ForeignKey(
        to='Branch',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_branch',
    )
    date = models.DateTimeField(null=False, auto_now_add=True)
    products = models.ManyToManyField(
        to='cruds.Product',
        through='core.SaleItem'
    )
    objects = managers.SaleManager()

    class Meta:
        db_table = 'sale'
        managed = True


class SaleItem(ModelBase):
    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_sale',
    )
    product = models.ForeignKey(
        to='cruds.Product',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_product',
    )
    quantity = models.DecimalField(decimal_places=3, max_digits=16, null=False)

    class Meta:
        db_table = 'sale_item'
        managed = True
