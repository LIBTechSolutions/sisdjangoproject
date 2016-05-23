from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

ACCESS_METHOD_CHOICE = (
    (u"HTTP GET", u"HTTP GET"),
    (u"HTTP POST", u"HTTP POST"),
    (u"FTP", u"FTP"),
    (u"SFTP", u"SFTP"),
    (u"GOOGLE DRIVE", u"GOOGLE DRIVE")
    (u"S3", u"S3"),
    (u"EMAIL", u"EMAIL"),
)

# ToDo
COMPRESSION_CHOICES = (
)


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

    access_method = models.CharField(
        _('Access Method'),
        max_length=30,
        choices=ACCESS_METHOD_CHOICE,
        default=u"HTTP GET",
        null=False,
        blank=False
    )

    availability = models.BoolField(
        _('Availability'),
        default=True,
        null=True,
        blank=True
    )

    # ToDo
    compression = models.CharField(
        _('Compression'),
        max_length=30,
        choices=COMPRESSION_CHOICES,
        default=u'',
        null=False,
        blank=False
    )

    description = models.TextField(
        _('Description'),
        null=False,
        blank=False
    )
