# Base Imports
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField
from model_utils.models import TimeStampedModel
from order_system.utils.choice import USER_TYPE
from django.utils.translation import ugettext_lazy as _


class User(TimeStampedModel, AbstractUser):
    """User model

    Extend form django Abstract user, change the username field to email and
    add some extra fields
    """

    email = EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    pais = CharField(default='chile', max_length=100)
    type = CharField(max_length=15, choices=USER_TYPE, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username"""
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

        permissions = [
            ('can_list_user', 'Can List user')
        ]
