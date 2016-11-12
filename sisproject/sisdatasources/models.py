from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _


GENDER_CHOICES = (
    (u"MALE", u"MALE"),
    (u"FEMALE", u"FEMALE"),
)


COUNTY_CHOICES = (
    (u"BOMI", u"BOMI"),
    (u"BONG", u"BONG"),
    (u"GBARPOLU", u"GBARPOLU"),
    (u"GRAND BASSA", u"GRAND BASSA"),
    (u"GRAND GEDEH", u"GRAND GEDEH"),
    (u"GRAND KRU", u"GRAND KRU"),
    (u"GRAND CAPE MOUNT", u"GRAND CAPE MOUNT"),
    (u"MARGIBI", u"MARGIBI"),
    (u"MARYLAND", u"MARYLAND"),
    (u"MONTSERRADO", u"MONTSERRADO"),
    (u"NIMBA", u"NIMBA"),
    (u"LOFA", u"LOFA"),
    (u"RIVERCESS", u"RIVERCESS"),
    (u"RIVERGEE", u"RIVERGEE"),
    (u"SINOE", u"SINOE"),
)

LEVEL_CHOICES = (
    (u"ELEMENTARY", u"ELEMENTARY"),
    (u"JUNIOR HIGH", u"JUNIOR HIGH"),
    (u"SENIOR HIGH", u"SENIOR HIGH"),
)

CLASS_CHOICES = (
    (u"10th", u"10th"),
    (u"11th", u"11th"),
    (u"12th", u"12th"),
)

SUBJECT_CHOICES = (
    (u"ENGLISH", u"ENGLISH"),
    (u"MATH", u"MATH"),
    (u"HISTORY", u"HISTORY"),
)

SCHEDULE_CHOICES = (
    (u"MONDAY", u"MONDAY"),
    (u"TUESDAY", u"TUESDAY"),
    (u"WEDNESDAY", u"WEDNESDAY"),
)


class Registration(models.Model):

    """
    This represents a single registration for each student.
    An entry must be done for every student who intends to register
    for admission.
    """

    lastName = models.CharField(
        _('Last Name'),
        max_length=30,
        null=False,
        blank=False
    )

    middleName = models.CharField(
        _('Middle Name'),
        max_length=30,
        null=True,
        blank=True
    )

    firstName = models.CharField(
        _('First Name'),
        max_length=30,
        null=False,
        blank=False
    )

    gender = models.CharField(
        _('Gender'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number format: '+999999999'. Up to 15 digits allowed."

    )
    phone_number = models.CharField(
        _('Phone Number'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    email = models.EmailField(
        _('Email Address'),
        max_length=254,
        null=True,
        blank=True
    )

    address = models.CharField(
        _('Address'),
        max_length=255,
        null=False,
        blank=False
    )

    city = models.CharField(
        _('City'),
        max_length=30,
        null=False,
        blank=False
    )

    county = models.CharField(
        _('County'),
        max_length=30,
        choices=COUNTY_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    nationality = models.CharField(
        _('Nationality'),
        max_length=30,
        null=False,
        blank=False
    )

    dateOfBirth = models.DateField(
        _('Date of Birth'),
        max_length=30,
        null=False,
        blank=False
    )

    placeOfBirth = models.CharField(
        _('Place of Birth'),
        max_length=255,
        null=False,
        blank=False
    )

    country = models.CharField(
        _('Country'),
        max_length=255,
        null=False,
        blank=False
    )

    emergency = models.CharField(
        _('Emergency Contact'),
        max_length=255,
        null=True,
        blank=True
    )

    emergency_phone = models.CharField(
        _('Phone (Emergency Contact)'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    previous_school = models.CharField(
        _('Previous School Attended'),
        max_length=255,
        null=False,
        blank=False
    )

    transcript = models.FileField(
        _('Transcript'),
        max_length=255,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.firstName


class Student(models.Model):

    """
    This represents a single student who has decided to enrol.
    It's a foreign key to registration and will get the remaining info
    from the registration table.
    """

    registration = models.ForeignKey(
        Registration
    )

    level = models.CharField(
        _('Level'),
        max_length=255,
        choices=LEVEL_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    grade = models.CharField(
        _('Class'),
        max_length=255,
        choices=CLASS_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    student_photo = models.FileField(
        _('Picture'),
        max_length=255,
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.level


class Teacher(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    teacherID = models.CharField(
        _('Teacher ID'),
        max_length=30,
        blank=True,
        default=''

    )

    lastName = models.CharField(
        _('Last Name'),
        max_length=30,
        null=False,
        blank=False
    )

    middleName = models.CharField(
        _('Middle Name'),
        max_length=30,
        null=True,
        blank=True
    )

    firstName = models.CharField(
        _('First Name'),
        max_length=30,
        null=False,
        blank=False
    )

    gender = models.CharField(
        _('Gender'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number format: '+999999999'. Up to 15 digits allowed."

    )

    phone_number = models.CharField(
        _('Phone Number'),
        max_length=255,
        validators=[phone_regex],
        blank=True
    )

    email = models.EmailField(
        _('Email Address'),
        max_length=254,
        null=True,
        blank=True
    )

    dateOfBirth = models.DateField(
        _('Date of Birth'),
        max_length=30,
        null=False,
        blank=False
    )

    placeOfBirth = models.CharField(
        _('Place of Birth'),
        max_length=255,
        null=False,
        blank=False
    )

    nationality = models.CharField(
        _('Nationality'),
        max_length=255,
        null=False,
        blank=False
    )

    qualification = models.CharField(
        _('Highest Qualification'),
        max_length=255,
        null=False,
        blank=False
    )

    experience = models.CharField(
        _('Experience in years'),
        max_length=255,
        null=False,
        blank=False
    )

    licence = models.CharField(
        _('Licence'),
        max_length=255,
        null=False,
        blank=False
    )

    teacher_photo = models.FileField(
        _('Teacher Picture'),
        max_length=255,
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.teacherID

    def save(self, force_insert=False, force_update=False):
        if self.teacherID == "":
            existing_teacherIDs = Teacher.objects.all().order_by('-teacherID')
            if existing_teacherIDs.count() > 0:
                new_code = int(existing_teacherIDs[0].teacherID[1:]) + 1
            else:
                new_code = 0
            self.teacherID = 'T%03d' % new_code
        super(Teacher, self).save(force_insert, force_update)

    def age(self):
        import datetime
        return int((datetime.date.today() - self.dateOfBirth).days / 365.25)


class Subject(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    teacher_ID = models.ForeignKey(
        Teacher,
        null=True
    )

    subject = MultiSelectField(
        _('Subject'),
        max_length=5,
        max_choices=5,
        choices=SUBJECT_CHOICES,
        blank=False,
        null=False,
        default=u' '

    )

    schedule = MultiSelectField(
        _('Teacher Schedule'),
        max_length=5,
        max_choices=5,
        choices=SCHEDULE_CHOICES,
        blank=False,
        null=False,
        default=u' '
    )

    teacher = models.ForeignKey(
        Student
    )

    def __str__(self):
        return self.subject
