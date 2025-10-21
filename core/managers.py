from django.db import models
from django.db.models import F, Case, When, Value, ExpressionWrapper, Func, OuterRef, Subquery, Count
from django.db.models.fields import FloatField
from django.db.models.functions import Now

from core.functions import Age
from core import models as core_models


class CustomerQuerySet(models.QuerySet):
    def filter_by_gender(self, gender):
        return self.filter(gender=gender)

    def gender_description(self):
        queryset = self.annotate(
            gender_description=Case(
                When(gender=Value('M'), then=Value('Masculino')),
                default=Value('Feminino')
            )
        )
        return queryset

    def get_income_customers_25_percentage(self):
        partial_income = ExpressionWrapper(F('income') * Value(0.25), output_field=FloatField())
        queryset = self.annotate(
            new_income=ExpressionWrapper(F('income') + partial_income, output_field=FloatField()),
        )
        return queryset.values('name', 'income', 'new_income')

    def gender_count(self, gender):
        return self.filter_by_gender(gender=gender).count()

    def ranking_top_5(self):
        return self.order_by('-income')[:5]

    def gt_10000(self):
        return self.filter(income__gt=10000)


class EmployeeQuerySet(models.QuerySet):
    def ranking_top_10(self):
        return self.order_by('-salary')[:10]

    def masters_employees(self):
        return self.annotate(
            age=Age('birth_date'),
        ).order_by('-age')

    def get_total_by_gender(self):
        return self.values('gender').annotate(
            total=Count('*'),
        ).values('gender', 'total')


class CustomerManager(models.Manager):

    def get_queryset(self, using=None, hints=None):
        return CustomerQuerySet(self.model, using=using, hints=hints)

    def gender_description(self):
        return self.get_queryset().gender_description()

    def filter_by_gender(self, gender):
        return self.get_queryset().filter_by_gender(gender=gender)

    def gender_count(self, gender):
        return self.get_queryset().gender_count(gender=gender)

    def ranking_top_5(self):
        return self.get_queryset().ranking_top_5()

    def gt_10000(self):
        return self.get_queryset().gt_10000()

    def count_by_marital_status(self):
        return self.values('marital_status__name').annotate(total=models.Count('*')).values(
            'marital_status__name', 'total'
        )

    def get_income_customers_25_percentage(self):
        return self.get_queryset().get_income_customers_25_percentage()


class EmployeeManager(models.Manager):
    def get_queryset(self, using=None, hints=None):
        return EmployeeQuerySet(self.model, using=using, hints=hints)

    def ranking_top_10(self):
        return self.get_queryset().ranking_top_10()

    def masters_employees(self):
        return self.get_queryset().masters_employees()

    def count_by_marital_status(self):
        return self.get_queryset().count_by_marital_status()

    def get_total_by_gender(self):
        return self.get_queryset().get_total_by_gender()


class SaleQuerySet(models.QuerySet):
    def gain_by_product_group(self, year: int, month: int):
        total_sale = ExpressionWrapper(
            F('saleitem__product__sale_price') * F('saleitem__quantity'),
            output_field=models.FloatField()
        )

        gain_sale = ExpressionWrapper(
            total_sale * (F('saleitem__product__product_group__gain_percentage') / Value(100)),
            output_field=models.FloatField()
        )

        return self.prefetch_related(
            'saleitem',
            'saleitem__product',
            'saleitem__product__product_group'
        ).values('saleitem__product__product_group__name').annotate(
            total=models.Sum(gain_sale)
        ).filter(
            date__year=year,
            date__month=month
        )


class SaleManager(models.Manager):
    def get_queryset(self, using=None, hints=None):
        return SaleQuerySet(self.model, using=using, hints=hints)

    def gain_by_product_group(self, year: int, month: int):
        return self.get_queryset().gain_by_product_group(year=year, month=month)
