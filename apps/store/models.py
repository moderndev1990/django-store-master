from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Store(BaseModel):
    """ enums """

    """ validators """

    """ fields """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='stores',
        verbose_name=_('owner'),
    )
    name = models.CharField(_('Name'), max_length=50)
    description = models.TextField(_('Description'), max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')

    def __str__(self):
        return self.name
