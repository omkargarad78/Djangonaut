from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email_notification(subject, message, recipient):
    try:
        logger.info(f"Sending email to {recipient} with subject: {subject}")
        send_mail(
            subject,
            message,
            "garadomkar78@gmail.com",  # Your sender email
            recipient,
            fail_silently=False,
        )
        logger.info("Email sent successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False