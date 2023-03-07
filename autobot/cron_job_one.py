from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import cron_job_two

""" Test cron job """

def send_test_email():
    body = 'test'
    subject = 'test'
    
    to_address = 'kristian@starsystems.ie'
    msg = EmailMessage(body=body, subject=subject, from_email=settings.DEFAULT_FROM_EMAIL, to=[to_address])
    msg.send()
    

