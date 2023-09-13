import time

from celery import shared_task
from celery_singleton import Singleton
from django.db.models import F


@shared_task(base=Singleton)
def set_price(subscription_id):
    from servises.models import Subscriptions
    time.sleep(5)  # Типа сложные расчеты

    subscription = Subscriptions.objects.filter(id=subscription_id).annotate(
        annotate_price=F('service__full_price') - F('service__full_price') * (
                    F("plan__discount_percent") / 100.00)).first()

    subscription.price = subscription.annotate_price
    subscription.save()
