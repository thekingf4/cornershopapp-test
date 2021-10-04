from django.db import models


class MetaDataInfo(models.Model):
    """Add metadata for only table

    metadata  acts as an abstract base class from which every other model in
    the project will inherit. this class provides every table with the following
    attributes:
    created_at (Datetime): Store the datetime the object was created
    update_at (Datetime): Store the last datetime the object was created
    """

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'update_at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta options"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
