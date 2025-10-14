from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.models import Sale, SaleItem


@receiver(pre_save, sender=SaleItem, weak=False, dispatch_uid='pre_save_run_sale_item')
def pre_save_run_sale_item(**kwargs):
    instance = kwargs.get('instance')
    instance.set_product_sale_price()
    instance.calculate_subtotal()
