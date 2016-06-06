from __future__ import unicode_literals

from django.db import models
from users.models import Contact
from users.models import Tenant
from django.utils.translation import ugettext as _


ACCESS_METHOD_CHOICE = (
    (u"HTTP GET", u"HTTP GET"),
    (u"HTTP POST", u"HTTP POST"),
    (u"FTP", u"FTP"),
    (u"SFTP", u"SFTP"),
    (u"GOOGLE DRIVE", u"GOOGLE DRIVE"),
    (u"S3", u"S3"),
    (u"EMAIL", u"EMAIL"),
)

AVAILABILITY_CHOICE = (
    (u"Online", u"Online"),
    (u"Offline", u"Offline"),
)

COMPRESSION_CHOICES = (
    (u"DEFLATE", u"DEFLATE"),
    (u"LZ", u"LZ"),
    (u"LZR", u"LZR"),
    (u"LZW", u"LZW"),
)

ENCODING_CHOICES = (
    (u"UTF-8", u"UTF-8"),
    (u"US-ASCII", u"US-ASCII"),
    (u"UTF-16", u"UTF-16"),
    (u"UTF-32", u"UTF-32"),
)

LANGUAGE_CHOICES = (
    (u"English", u"English"),
    (u"Arabic", u"Arabic"),
    (u"French", u"French"),
    (u"German", u"German"),
    (u"Portuguese", u"Portuguese"),
    (u"Spanish", u"Spanish"),
)

SCHEMA_TYPE_CHOICES = (
    (u"None", u"None"),
    (u"Column Headers", u"Column Headers"),
    (u"AVRO", u"AVRO"),
    (u"HXL", u"HXL"),
    (u"JSON-LD", u"JSON-LD"),
    (u"RDF", u"RDF"),
    (u"XML", u"XML"),
)


class Source(models.Model):

    """
    A source is a single data structure/type from a single application that
    sends data to the HIS data warehouse.  E.g. lab results from an LIS
    application
    """

    tenant_id = models.ManyToManyField(
        'users.Tenant',
        related_query_name='source',
        blank=False,
    )

    contact_id = models.OneToOneField(
        'users.Contact',
        related_name='sources',
        related_query_name='source',
        null=False,
        blank=False,
    )

    access_method = models.CharField(
        _('Description of access protocol'),
        max_length=30,
        choices=ACCESS_METHOD_CHOICE,
        default=u' ',
        null=False,
        blank=False
    )

    availability = models.CharField(
        _('Last known availability'),
        max_length=30,
        choices=AVAILABILITY_CHOICE,
        default=u' ',
        null=True,
        blank=True
    )

    compression = models.CharField(
        _('Compression algorithm used with source'),
        max_length=30,
        choices=COMPRESSION_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    description = models.TextField(
        _('Link to digital rights document (e.g. contract)'),
        null=False,
        default=' ',
        blank=False
    )

    digital_rights = models.URLField(
        _('Overview of the data source (provided by maintainer)'),
        max_length=100,
        null=False,
        default=' ',
        blank=False
    )

    encoding = models.CharField(
        _('Character encoding (e.g. UTF-8)'),
        max_length=30,
        choices=ENCODING_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    encryption = models.CharField(
        _('Name / link to encryption algorithm used'),
        max_length=100,
        default=' ',
        null=True,
        blank=True
    )

    language = models.CharField(
        _('Language in which the data is written'),
        max_length=30,
        choices=LANGUAGE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    last_accessed = models.DateField(
        _('Last known access'),
        auto_now=True,
        null=True,
        blank=True
    )

    last_modified = models.DateField(
        _('Last record update'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    last_refreshed = models.DateField(
        _('Last known refresh date'),
        auto_now=False,
        default=' ',
        null=False,
        blank=False
    )

    license_type = models.URLField(
        _('Name of primary business contact'),
        max_length=100,
        default=' ',
        null=False,
        blank=False
    )

    maintainer = models.CharField(
        _('License type (e.g. Open Data Commons)'),
        max_length=30,
        default=' ',
        null=False,
        blank=False
    )

    pii = models.BooleanField(
        _('Does source contain personally-identifiable information?'),
        default=False,
        null=False,
        blank=False
    )

    records = models.BigIntegerField(
        _('Last known record count'),
        default=' ',
        null=True,
        blank=True
    )

    json_schema = models.TextField(
        _('RegEx expression used with access method'),
        max_length=30,
        default=' ',
        null=True,
        blank=True
    )

    schema_type = models.CharField(
        _('Schema type used to describe data source attributes'),
        max_length=30,
        choices=SCHEMA_TYPE_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    size = models.BigIntegerField(
        _('Last known size (MB)'),
        default=' ',
        null=True,
        blank=True
    )

    system_of_record = models.BooleanField(
        _('Is this is a primary resource? (i.e. not a replica or extract)'),
        max_length=30,
        default=False,
        null=False,
        blank=True
    )

    uri_access = models.URLField(
        _('Access URI for data'),
        max_length=100,
        default=' ',
        null=False,
        blank=False
    )

    uri_documenation = models.URLField(
        _('Link to API documentation'),
        max_length=100,
        default=' ',
        null=True,
        blank=True
    )

    uri_endpoint = models.URLField(
        _('Access URI for endpoint API'),
        max_length=100,
        default=' ',
        null=True,
        blank=True
    )

    uri_schema = models.URLField(
        _('Access URI for schema (supply if schema_type is not "None")'),
        max_length=100,
        default=' ',
        null=True,
        blank=True
    )

    title = models.CharField(
        _('Descriptive title (provided by maintainer)'),
        max_length=255,
        default=' ',
        null=False,
        blank=False
    )

    visibility = models.BooleanField(
        _('Visible in view service'),
        default=True,
        null=False,
        blank=False
    )
