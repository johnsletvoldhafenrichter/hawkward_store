from django.urls import path
from . import views
from .webhooks import webhook_received

urlpatterns = [
    path('', views.check_for_free_items, name='check_for_free_items'),
    path('payment/', views.payment,
         name='payment'),
    path('payment_method/', views.payment_method,
         name='payment_method'),
    path('payment_backend/', views.payment_backend,
         name='payment_backend'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('subscription/', views.subscription, name='subscription'),
    path('wh/', webhook_received, name='webhook_received'),
    path('subscription/', views.subscription, name='subscription'),
    path('subscription_payment_method/', views.subscription_payment_method,
         name='subscription_payment_method'),
    path('subscription_backend/', views.subscription_backend,
         name='subscription_backend'),
    path('payment_error/', views.payment_error,
         name='payment_error'),
    path('delete_subscription/', views.delete_subscription,
         name='delete_subscription'),
    path('wherrors/', webhook_received,
         name='webhook_received'),
]
