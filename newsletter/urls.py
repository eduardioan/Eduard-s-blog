from django.urls import path
from .views import newsletter_subscribe, show_subscription

app_name = 'newsletter'
urlpatterns = [
      path('newsletter/subscribe/', newsletter_subscribe, name='subscribe'),
      path('newsletter/subscription-done/', show_subscription, name='subscription_done'),

]
