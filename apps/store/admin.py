from django.contrib import admin

from . import models


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'owner',
        'created',
    ]

    list_select_related = [
        'owner',
    ]

    readonly_fields = [
        'id',
        'created',
        'updated',
    ]
