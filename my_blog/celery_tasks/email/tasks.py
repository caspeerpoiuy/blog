from django.core.mail import send_mail
from celery_tasks.main import app


@app.task(name="send verify mail")
def send_verify_mail(subject, message, from_email, recipient_list, html_message):
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)