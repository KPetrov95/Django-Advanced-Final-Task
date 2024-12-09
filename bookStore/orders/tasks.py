from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from .. import settings


@shared_task
def send_order_confirmation_email(order_id, email):
    order = Order.objects.get(id=order_id)
    send_mail(subject=f'Order #{order.id} Confirmation',
              message=f"Hi {order.full_name},\n\n"
                      f"Thank you for your order!\n\n"
                      f"Order Details:\n"
                      f"Total Price: ${order.total_price}\n"
                      f"Delivery Address: {order.address}\n\n"
                      "We will notify you once the order is shipped.\n"
                      "Thank you for shopping with us!",
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email,],
              fail_silently=False
              )
