from model_utils import Choices
from django.utils.translation import ugettext_lazy as _

USER_TYPE = Choices(
    ('employees', _('Employees')),
    ('admin', _('Admin'))
)
