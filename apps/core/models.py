from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """ fields """
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta:
        abstract = True
