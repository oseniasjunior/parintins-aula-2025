from django.db.models import ExpressionWrapper, F, Value, FloatField

from core import models


def get_income_customers_25_percentage():
    partial_income = ExpressionWrapper(F('income') * Value(0.25), output_field=FloatField())
    queryset = models.Customer.objects.annotate(
        new_income=ExpressionWrapper(F('income') + partial_income, output_field=FloatField()),
    )
    return queryset.values('name', 'income', 'new_income')
