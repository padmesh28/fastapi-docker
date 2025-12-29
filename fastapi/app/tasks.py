from .celery_app import celery_app
import time

@celery_app.task(bind=True)
def long_running_task(self, value: int):
    time.sleep(5)
    return f"Processed value: {value}"

