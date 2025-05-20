from django.core.management.base import BaseCommand
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Test email sending functionality'

    def handle(self, *args, **options):
        try:
            self.stdout.write('Attempting to send test email...')
            
            result = send_mail(
                'Test Email from Django',
                'This is a test email from your Django application.',
                'garadomkar78@gmail.com',  # Your sender email
                ['garadomkar78@gmail.com'],  # Your recipient email
                fail_silently=False,
            )
            
            if result:
                self.stdout.write(self.style.SUCCESS('Email sent successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Email was not sent.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending email: {str(e)}'))