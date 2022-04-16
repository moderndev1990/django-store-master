from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Product(BaseModel):
    """ fields """
    store = models.ForeignKey(
        'store.Store',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Store',
    )
    name = models.CharField(_('Product'), max_length=64)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Image'), upload_to='product_images', blank=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-created',)

    def __str__(self):
        return self.name
