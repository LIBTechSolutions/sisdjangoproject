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

ENROLLMENT_CHOICES = (
    (u"ENROLLED", u"ENROLLED"),
    (u"DID NOT ENROLLED", u"DID NOT ENROLLED"),
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

POSITION_CHOICES = (
    (u"TEACHER", u"TEACHER"),
    (u"TEACHER", u"TEACHER"),
    (u"ACCOUNTANT", u"ACCOUNTANT"),
)

MONTH_CHOICES = (
    (u"JANUARY", u"JANUARY"),
    (u"FEBRUARY", u"FEBRUARY"),
    (u"MARCH", u"MARCH"),
    (u"APRIL", u"APRIL"),
    (u"MAY", u"MAY"),
    (u"JUNE", u"JUNE"),
    (u"JULY", u"JULY"),
    (u"AUGUST", u"AUGUST"),
    (u"SEPTEMBER", u"SEPTEMBER"),
    (u"OCTOBER", u"OCTOBER"),
    (u"NOVEMBER", u"NOVEMBER"),
    (u"DECEMBER", u"DECEMBER"),
)

SEMESTER_CHOICES = (
    (u"1st SEMESTER", u"1st SEMESTER"),
    (u"2nd SEMESTER", u"2nd SEMESTER"),
)

ACTIVE_CHOICES = (
    (u"YES", u"YES"),
    (u"NO", u"NO"),
)

PERIOD_CHOICES = (
    (u"1st PERIOD", u"1st PERIOD"),
    (u"2nd PERIOD", u"2nd PERIOD"),
    (u"3rd PERIOD", u"3rd PERIOD"),
    (u"1st SEMESTER EXAM", u"1st SEMESTER EXAM"),
    (u"4th PERIOD", u"4th PERIOD"),
    (u"5th PERIOD", u"5th PERIOD"),
    (u"6th PERIOD", u"6th PERIOD"),
    (u"2nd SEMESTER EXAM", u"2nd SEMESTER EXAM"),
)

RANK_CHOICES = (
    (u"PASSED", u"PASSED"),
    (u"FAILED", u"FAILED"),
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

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
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

    regDate = models.DateField(
        _('Registration Date'),
        max_length=30,
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

    def age(self):
        import datetime
        return int((datetime.date.today() - self.dateOfBirth).days / 365.25)


class Student(models.Model):

    """
    This represents a single student who has decided to enrol.
    It's a foreign key to registration and will get the remaining info
    from the registration table.
    """

    studentID = models.CharField(
        _('Student ID'),
        max_length=30,
        blank=True,
        default=''

    )

    registration = models.ForeignKey(
        Registration
    )

    student_photo = models.FileField(
        _('Picture'),
        max_length=255,
        null=False,
        blank=False
    )

    previous_school = models.CharField(
        _('Previous School Attended'),
        max_length=255,
        null=False,
        blank=False
    )

    previous_school_address = models.CharField(
        _('Previous School Address'),
        max_length=255,
        null=False,
        blank=False
    )

    last_year_attendance = models.DateField(
        _('Last Year of Attendance'),
        max_length=30,
        null=False,
        blank=False
    )

    level = models.CharField(
        _('Level'),
        max_length=255,
        choices=LEVEL_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    enrollment_status = models.CharField(
        _('Enrollment Status'),
        max_length=255,
        choices=ENROLLMENT_CHOICES,
        default=None,
        null=False,
        blank=False
    )

    enrollment_Date = models.DateField(
        _('Enrollment Date'),
        max_length=30,
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
        return self.studentID

    def save(self, force_insert=False, force_update=False):
        if self.studentID == "":
            existing_studentIDs = Student.objects.all().order_by('-studentID')
            if existing_studentIDs.count() > 0:
                new_code = int(existing_studentIDs[0].studentID[1:]) + 1
            else:
                new_code = 0
            self.studentID = 'S%03d' % new_code
        super(Student, self).save(force_insert, force_update)


class Parent(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    parentID = models.CharField(
        _('Parent ID'),
        max_length=30,
        blank=True,
        default=''

    )

    student = models.ForeignKey(
        Student
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

    address = models.CharField(
        _('Address'),
        max_length=255,
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

    nationality = models.CharField(
        _('Nationality'),
        max_length=255,
        null=True,
        blank=True
    )

    occupation = models.CharField(
        _('Occupation'),
        max_length=255,
        null=True,
        blank=True
    )

    entity_name = models.CharField(
        _('Name of Entity'),
        max_length=255,
        null=True,
        blank=True
    )

    entity_address = models.CharField(
        _('Entity Address'),
        max_length=255,
        null=True,
        blank=True
    )

    salary_range = models.IntegerField(
        _('Salary Range'),
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
        return self.parentID

    def save(self, force_insert=False, force_update=False):
        if self.parentID == "":
            existing_parentIDs = Parent.objects.all().order_by('-parentID')
            if existing_parentIDs.count() > 0:
                new_code = int(existing_parentIDs[0].parentID[1:]) + 1
            else:
                new_code = 0
            self.parentID = 'S%03d' % new_code
        super(Parent, self).save(force_insert, force_update)


class Staff(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    staffID = models.CharField(
        _('Staff ID'),
        max_length=30,
        blank=True,
        default=''

    )

    staff_photo = models.FileField(
        _('Teacher Picture'),
        max_length=255,
        null=False,
        blank=False
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

    numberOfSubject = models.IntegerField(
        _('Number of Subject Teaching'),
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
        return self.staffID

    def save(self, force_insert=False, force_update=False):
        if self.staffID == "":
            existing_staffIDs = Staff.objects.all().order_by('-staffID')
            if existing_staffIDs.count() > 0:
                new_code = int(existing_staffIDs[0].staffID[1:]) + 1
            else:
                new_code = 0
            self.staffID = 'ST%03d' % new_code
        super(Staff, self).save(force_insert, force_update)

    def age(self):
        import datetime
        return int((datetime.date.today() - self.dateOfBirth).days / 365.25)


class Staff_Position(models.Model):

    """
    This represents a single teacher.
    He/she is teaching many subjects and classes.
    """

    staff = models.ForeignKey(
        Staff
    )

    departmentName = MultiSelectField(
        _('Staff Position'),
        max_length=5,
        max_choices=5,
        choices=POSITION_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.departmentName


class Grade(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    grade = models.CharField(
        _('Class'),
        max_length=30,
        choices=GENDER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    sponsor = models.ForeignKey(
        Staff
    )

    totalNumberOfStudents = models.IntegerField(
        _('Total Number of Students'),
        blank=False,
        null=False,
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.grade


class Subject(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    staff = models.ForeignKey(
        Staff,
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

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.subject


class Payment(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    ReceiptNo = models.CharField(
        _('Receipt Number'),
        max_length=30,
        blank=True,
        default=''

    )

    digitalSignature = models.CharField(
        _('Digital Signature'),
        max_length=255,
        null=True,
        blank=True
    )

    totalyearlyfee = models.IntegerField(
        _('Total Yearly Fee'),
        null=True,
        blank=True
    )

    totalfirstsemesterfee = models.IntegerField(
        _('Total First Semester Fee'),
        null=True,
        blank=True
    )

    totalsecondsemesterfee = models.IntegerField(
        _('Total Second Semester Fee')
    )

    firstpayment = models.IntegerField(
        _('First Payment'),
        default=0,
        null=True,
        blank=True
    )

    secondpayment = models.IntegerField(
        _('Second Payment'),
        default=0,
        null=True,
        blank=True
    )

    totalfirstsemesterpayment = models.IntegerField(
        _('Total First Semester Payment')
    )

    firstsemesterbalance = models.IntegerField(
        _('First Semester Balance')
    )

    thirdpayment = models.IntegerField(
        _('Third Payment'),
        default=0,
        null=True,
        blank=True
    )

    fourthpayment = models.IntegerField(
        _('Fourth Payment'),
        default=0,
        null=True,
        blank=True
    )

    totalsecondsemesterpayment = models.IntegerField(
        _('Total First Semester Payment')
    )

    secondsemesterbalance = models.IntegerField(
        _('Second Semester Balance')
    )

    totalyearlypayment = models.IntegerField(
        _('Total Yearly Payment')
    )

    totalyearlybalance = models.IntegerField(
        _('Total Yearly Balance')
    )

    transaction_Date = models.DateField(
        _('Date of Transaction'),
        auto_now=True,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.ReceiptNo

    def save(self, force_insert=False, force_update=False):
        if self.ReceiptNo == "":
            existing_ReceiptNos = Payment.objects.all().order_by('-ReceiptNo')
            if existing_ReceiptNos.count() > 0:
                new_code = int(existing_ReceiptNos[0].ReceiptNo[1:]) + 1
            else:
                new_code = 0
            self.ReceiptNo = 'R%03d' % new_code
        super(ReceiptNo, self).save(force_insert, force_update)

    def save(self, *args, **kwargs):
        self.totalsecondsemesterfee = self.totalyearlyfee - self.totalfirstsemesterfee
        super(Payment, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.totalfirstsemesterpayment = self.firstpayment + self.secondpayment
        super(Payment, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.firstsemesterbalance = self.totalfirstsemesterfee - self.totalfirstsemesterpayment
        super(Payment, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.totalsecondsemesterpayment = self.thirdpayment + self.fourthpayment
        super(Payment, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.secondsemesterbalance = self.totalsecondsemesterfee - self.totalsecondsemesterpayment
        super(Payment, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.totalyearlypayment = self.totalfirstsemesterpayment + self.totalsecondsemesterpayment
        super(Payment, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.totalyearlybalance = self.totalyearlyfee - self.totalyearlypayment
        super(Payment, self).save(*args, **kwargs)


class Payroll(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    staff = models.ForeignKey(
        Staff
    )

    accountnumber = models.CharField(
        _('Account Number'),
        max_length=255,
        null=False,
        blank=False
    )

    grossmonthlysalary = models.IntegerField(
        _('Monthly Salary'),
        null=False,
        blank=False
    )

    contractperiod = models.IntegerField(
        _('Contract Period'),
        null=False,
        blank=False
    )

    grossannualsalary = models.IntegerField(
        _('Gross Annual Salary')
    )

    monthlyincometax = models.IntegerField(
        _('Monthly Income Tax')
    )

    netmonthlysalary = models.IntegerField(
        _('Net Monthly Salary')
    )

    month = models.CharField(
        _('Month Paid For'),
        max_length=30,
        choices=MONTH_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    salaryDate = models.DateField(
        _('Paid Date'),
        auto_now=True,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.grossannualsalary = self.grossmonthlysalary * contractperiod
        super(Payroll, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.monthlyincometax = self.grossmonthlysalary * 0.1
        super(Payroll, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.netmonthlysalary = self.grossmonthlysalary - monthlyincometax
        super(Payroll, self).save(*args, **kwargs)


class AcademicYear(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    import datetime
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    year = models.IntegerField(
        _('Academic Year'),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    semester = models.CharField(
        _('Semester'),
        max_length=30,
        choices=SEMESTER_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    student = models.ForeignKey(
        Student
    )

    isactive = models.CharField(
        _('Is Active'),
        max_length=30,
        choices=ACTIVE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.year


class StudentMark(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    year = models.ForeignKey(
        AcademicYear
    )

    subject = models.ForeignKey(
        Subject
    )

    peroid = models.CharField(
        _('Period Test'),
        max_length=30,
        choices=PERIOD_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    gradeScore = models.CharField(
        _('Grade Scored'),
        max_length=30,
        blank=True,
        default=''

    )

    studenRank = models.CharField(
        _('Student Rank'),
        max_length=30,
        blank=True,
        default=''

    )

    status = models.CharField(
        _('Status'),
        max_length=30,
        choices=RANK_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.grade


class ClassSchedule(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    grade = models.ForeignKey(
        Grade
    )

    day = models.CharField(
        _('Days'),
        max_length=30,
        choices=SCHEDULE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    classTime = models.DateTimeField(
        _('Class Time'),
        null=True,
        blank=True

    )

    year = models.ForeignKey(
        AcademicYear
    )

    subject = models.ForeignKey(
        Subject
    )

    staff = models.ForeignKey(
        Staff
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )


class StudentAttendance(models.Model):

    """
    This represents subjects.
    Subjects will be taught by teachers.
    """

    student = models.ForeignKey(
        Student
    )

    year = models.ForeignKey(
        AcademicYear
    )

    grade = models.ForeignKey(
        Grade
    )

    present = models.CharField(
        _('Present'),
        max_length=30,
        choices=ACTIVE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    absent = models.CharField(
        _('Absent'),
        max_length=30,
        choices=ACTIVE_CHOICES,
        default=u' ',
        null=False,
        blank=False
    )

    reasonAbsent = models.TextField(
        _('Reason Absent'),
        max_length=255,
        blank=True,
        default=''

    )

    absentDate = models.DateField(
        _('Date'),
        auto_now=True,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
