from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task(name='email')
def mail():
    subject = 'welcome to Stexity'

    message = f'Hi hyder, thank you for \
        registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ha03172046587@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    
