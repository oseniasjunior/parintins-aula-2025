from celery import shared_task
from core import actions


@shared_task(bind=True, queue='default')
def create_customers_report(self):
    actions.CustomerAction.create_report()
