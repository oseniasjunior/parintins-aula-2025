from django.utils.timezone import now

from core import models


class CustomerAction:
    @staticmethod
    def create_report():
        customers = models.Customer.objects.all()
        _now = now()
        with open(f'/tmp/customers_{_now.year}{_now.month}{_now.day}{_now.hour}{_now.minute}.csv', 'w+') as file:
            for customer in customers:
                file.write(f'{customer.id};{customer.name}\n')
