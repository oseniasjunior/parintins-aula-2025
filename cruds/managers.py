from django.db import models
from django.db.models import OuterRef, Subquery
from core import models as core_models


class ProductQuerySet(models.QuerySet):
    def with_last_sale(self):
        subquery = core_models.SaleItem.objects.filter(
            product=OuterRef('id')
        ).order_by('-sale__date').values('sale__date')[:1]
        return self.annotate(last_sale=Subquery(subquery)).values('name', 'last_sale')


class ProductManager(models.Manager):
    def get_queryset(self, using=None, hints=None):
        return ProductQuerySet(self.model, using=using, hints=hints)

    def with_last_sale(self):
        return self.get_queryset().with_last_sale()
