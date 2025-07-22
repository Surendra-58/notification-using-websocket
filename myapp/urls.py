from django.urls import path
from .views import admin_notify, user_notification

urlpatterns = [
    path('notify/', admin_notify, name='admin_notify'),
    path('<str:username>/', user_notification, name='user_notification'),
]
