from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Tenant(models.Model):

    """
    Model to represent a single Tenant.  A Tenant is a person or an
    organisation that is responsible for an application that contributes data
    to the HIS data warehouse
    """

    name = models.CharField(
        _('Name of Organisation'),
        max_length=100,
        null=False,
        blank=False
    )

    contact = models.CharField(
        _('Name of contact person at the Organisation'),
        max_length=100,
        null=False,
        blank=False
    )

    email = models.EmailField(
        _('Email Address of contact at the Organisation'),
        null=False,
        blank=False
    )

    phone_number = models.CharField(
        _('Phone Number of contact at the Organisation'),
        max_length=20,
        null=True,
        blank=True
    )

    url = models.CharField(
        _('URL of the Organisation'),
        max_length=256,
        null=True,
        blank=True
    )
