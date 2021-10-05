# Base Imports
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField


class User(AbstractUser):
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
    pais = CharField(
        default='chile',
        max_length=100
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username"""
        return self.username

    @property
    def is_employees(self):
        return True

    class Meta:
        permissions = [('can_users', 'Can users')]
