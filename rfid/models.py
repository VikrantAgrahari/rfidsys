# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45, blank=True, null=True)
    contact = models.IntegerField()
    country = models.CharField(max_length=45)

    class Meta:
        #managed = False
        db_table = 'address'

class Assesment(models.Model):
    ass_id = models.CharField(unique=True, max_length=45)
    sub = models.ForeignKey('Subjects', models.DO_NOTHING, default='01')
    type = models.CharField(max_length=45)
    date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'assesment'
        unique_together = (('id', 'ass_id'),)


class Attendance(models.Model):
    std_roll = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='std_roll', default='01')
    sub = models.ForeignKey('Subjects', models.DO_NOTHING, default='01')
    tea = models.ForeignKey('Teachers', models.DO_NOTHING, default='01')
    date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'attendance'
        unique_together = (('id', 'std_roll', 'sub', 'tea'),)



class BookIssue(models.Model):
    book = models.ForeignKey('Books', models.DO_NOTHING,default='01')
    std_roll = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='std_roll', default='01')
    issue_date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'book_issue'


class BookReturn(models.Model):
    book = models.ForeignKey('Books', models.DO_NOTHING, default='01')
    std_roll = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='std_roll', default='01')
    return_date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'book_return'


class Books(models.Model):
    book_id = models.CharField(unique=True, max_length=45)
    book_name = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    publication = models.CharField(max_length=45)
    purchase_date = models.DateField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'books'
        unique_together = (('id', 'book_id'),)


class Deposit(models.Model):
    user = models.ForeignKey('PaymentAccount', models.DO_NOTHING, default='01')
    amount_total = models.IntegerField()
    date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'deposit'
        unique_together = (('id', 'user'),)


class DepositRecord(models.Model):
    user = models.ForeignKey('PaymentAccount', models.DO_NOTHING, default='01')
    amount = models.IntegerField()
    deposit_date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'deposit_record'


class Marks(models.Model):
    std_roll = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='std_roll', default='01')
    sub = models.ForeignKey('Subjects', models.DO_NOTHING, default='01')
    ass = models.ForeignKey(Assesment, models.DO_NOTHING, default='01')
    tea = models.ForeignKey('Teachers', models.DO_NOTHING, default='01')
    mark = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'marks'


class Parent(models.Model):
    parent_id = models.CharField(unique=True, max_length=45)
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    dob = models.DateField()
    address = models.CharField(max_length=45)
    photo = models.CharField(max_length=45, blank=True, null=True)
    profession = models.CharField(max_length=45)

    class Meta:
        #managed = False
        db_table = 'parent'
        unique_together = (('id', 'parent_id'),)


class PaymentAccount(models.Model):
    user = models.ForeignKey('Teachers', models.DO_NOTHING, default='01')
    psw = models.CharField(max_length=60)
    created_date = models.CharField(max_length=45)

    class Meta:
       #managed = False
        db_table = 'payment_account'
        unique_together = (('id', 'user'),)


class PaymentRecord(models.Model):
    reader = models.ForeignKey('RfReader', models.DO_NOTHING, default='01')
    user = models.ForeignKey(PaymentAccount, models.DO_NOTHING, default='01')
    amount = models.IntegerField()
    date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'payment_record'


class RfReader(models.Model):
    reader_id = models.CharField(unique=True, max_length=45)
    purpose = models.CharField(max_length=45)
    install_date = models.DateField()

    class Meta:
        #managed = False
        db_table = 'rf_reader'
        unique_together = (('id', 'reader_id'),)


class StdSubs(models.Model):
    std_roll = models.ForeignKey('StudentInfo', models.DO_NOTHING, db_column='std_roll', default='01')
    sub_grade = models.CharField(max_length=45)

    class Meta:
        #managed = False
        db_table = 'std_subs'
        unique_together = (('id', 'std_roll'),)


class StudentInfo(models.Model):
    std_roll = models.CharField(unique=True, max_length=45)
    rftag = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    grade = models.CharField(max_length=45)
    dob = models.DateField()
    gender = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    enroll_date = models.DateField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey(Parent, models.DO_NOTHING, default='01')
    address = models.ForeignKey(Address, models.DO_NOTHING, default='01')

    class Meta:
        #managed = False
        db_table = 'student_info'
        unique_together = (('id', 'std_roll', 'address'),)


class Subjects(models.Model):
    sub_id = models.CharField(unique=True, max_length=45)
    sub_name = models.CharField(max_length=45)
    grade = models.CharField(max_length=45)
    type = models.CharField(max_length=45)

    class Meta:
        #managed = False
        db_table = 'subjects'
        unique_together = (('id', 'sub_id'),)


class TeaSub(models.Model):
    tea = models.ForeignKey('Teachers', models.DO_NOTHING, default='01')
    sub = models.ForeignKey('Subjects', models.DO_NOTHING, default='01')

    class Meta:
        #managed = False
        db_table = 'tea_sub'


class Teachers(models.Model):
    tea_id = models.CharField(unique=True, max_length=45)
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    rftag = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    dob = models.DateField()
    roll_type = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    photo = models.CharField(max_length=45, blank=True, null=True)
    address_0 = models.ForeignKey(Address, models.DO_NOTHING, db_column='address_id', default='01')  # Field renamed because of name conflict.

    class Meta:
        #managed = False
        db_table = 'teachers'
        unique_together = (('id', 'tea_id', 'address_0'),)