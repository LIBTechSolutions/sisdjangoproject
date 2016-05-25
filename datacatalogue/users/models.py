from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Tenant(models.Model):

    """
    Model to represent a single Tenant.  A Tenant is a person or an
    organisation that is responsible for an application that contributes data
    to the HIS data warehouse
    """

    role = models.CharField(
        _('Scope (used by view service)'),
        max_length=100,
        null=False,
        blank=False,
        default = "limited"
    )

    contact_id = models.ForeignKey(
        Contact,
        on_delete = models.CASCADE
    )

    email = models.EmailField(
        _('Email Address of contact at the Organisation'),
        null=False,
        blank=False
    )

    url = models.CharField(
        _('Tenant home page'),
        max_length=256,
        null=False,
        blank=False
    )


class LDAP(models.Model):

    """
    Model to represent a LDAP.  
    """

    dc = models.CharField(
        _('LDAP domainComponent (DC)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "DC="
    )
        
    cn = models.CharField(
         _('LDAP commonName (CN)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "CN="
    )

    ou = models.CharField(
         _('LDAP organizationalUnitName (OU)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "OU="
    )

    o = models.CharField(
         _('LDAP organizationalName (O)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "O="
    )

    street = models.CharField(
         _('LDAP streetAddress (STREET)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "STREET="
    )

    l = models.CharField(
         _('LDAP localityName (L)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "L="
    )

    street = models.CharField(
         _('LDAP stateOrProvinceName (ST)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "ST="
    )

    cn = models.CharField(
         _('LDAP countryName(C)'),
        max_length = 100,
        null = False,
        blank = False,
        default = "C="
    )

    uid = models.CharField(
         _('LDAP userId (UID)'),
        max_length = 100,
        default = "UID="
    )

    dn = models.AutoField(
         _('LDAP distinguishedName (DN)')
        
    )


class Contact(models.Model):

    """
    Model to represent a Contact.  
    """

    first_name = models.CharField(
         _('First name of contact'),
        max_length = 30,
        null = False,
        blank = False
    )

    last_name = models.CharField(
         _('Last name of contact'),
        max_length = 30,
        null = False,
        blank = False
    )

    email_address = models.EmailField(
        _('E-mail address of contact'),
        null = False,
        blank = False
    )

    phone_number = models.CharField(
        _('Phone number of contact'),
        max_length=20,
        null=False,
        blank=False
    )

    ldap_id = models.ForeignKey(
        LDAP,
        on_delete = models.CASCADE
    )

