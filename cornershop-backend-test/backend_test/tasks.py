from celery import Celery
from django.conf import settings
from datetime import timedelta
from order_system.utils.generators import Generator
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

__app = Celery()


@__app.task(name='send_recovery_password_email', max_retries=3)
def send_recovery_password_email(email, fullname, username):
    subject = 'Recover password'
    from_email = 'Recovery <info@company.com>'

    recovery_token = Generator.gen_token(
        data={'email': email},
        type='password_reset',
        time=timedelta(hours=2)
    )

    content = render_to_string(
        'emails/auth/recovery_password.html',
        {'fullname': fullname, 'token': recovery_token, 'url': settings.URL_EMAILS, 'username': username}
    )

    msg = EmailMultiAlternatives(subject, content, from_email, [email])
    msg.attach_alternative(content, "text/html")
    msg.send()
