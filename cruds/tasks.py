from celery import shared_task
from cruds import actions


@shared_task(bind=True, queue='default')
def create_state_file(self, state_id: int):
    actions.StateAction.create_state_file(state_id)
