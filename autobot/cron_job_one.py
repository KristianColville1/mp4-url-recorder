from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import cron_job_two

""" Test cron job """

def send_test_email():
    body = cron_job_two.body
    subject = cron_job_two.subject
    
    to_address = 'kristian.avss@gmail.com'
    msg = EmailMessage(body=body, subject=subject, from_email=settings.DEFAULT_FROM_EMAIL, to=[to_address])
    msg.send()
    

def main():
    send_test_email()

if __name__ == '__main__':
    main()