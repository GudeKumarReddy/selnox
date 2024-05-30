from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor
from django.utils.timezone import now

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    if instance.status == 'completed':
        update_on_time_delivery_rate(instance.vendor)
        update_fulfillment_rate(instance.vendor)
        if instance.quality_rating:
            update_quality_rating_avg(instance.vendor)

    if instance.acknowledgment_date:
        update_response_time(instance.vendor)

def update_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_orders = completed_orders.filter(delivery_date__lte=now())
    vendor.on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0
    vendor.save()

def update_quality_rating_avg(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    average_quality_rating = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']
    vendor.quality_rating_avg = average_quality_rating if average_quality_rating else 0
    vendor.save()

def update_response_time(vendor):
    orders_with_ack = PurchaseOrder.objects.filter(vendor=vendor).exclude(acknowledgment_date__isnull=True)
    total_response_time = sum([(order.acknowledgment_date - order.issue_date).total_seconds() for order in orders_with_ack])
    vendor.average_response_time = (total_response_time / orders_with_ack.count()) if orders_with_ack.count() > 0 else 0
    vendor.save()

def update_fulfillment_rate(vendor):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    vendor.fulfillment_rate = (completed_orders / total_orders) * 100 if total_orders > 0 else 0
    vendor.save()
