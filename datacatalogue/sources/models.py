from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class Source(models.Model):

    """
    A source is a single data structure/type from a single application that
    sends data to the HIS data warehouse.  E.g. lab results from an LIS
    application
    """

    tenant = models.ForeignKey(
        'tenants.Tenant',
        # I think we should always set this to NULL if we delete the tenant
        # because that way we can always post-process historical data
        on_delete=models.SET_NULL,
        related_name='sources',
        related_query_name='source',
        null=False,
        blank=False
    )
