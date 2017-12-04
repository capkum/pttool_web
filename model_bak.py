# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TbAdminaccount(models.Model):
    seq = models.IntegerField(primary_key=True, blank=True, null=True)
    accountid = models.CharField(db_column='accountId', max_length=24)  # Field name made lowercase.
    accountpw = models.CharField(db_column='accountPw', max_length=70)  # Field name made lowercase.
    accountnm = models.CharField(db_column='accountNm', max_length=10)  # Field name made lowercase.
    accountph = models.CharField(db_column='accountPh', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accountdpt = models.CharField(db_column='accountDpt', max_length=60, blank=True, null=True)  # Field name made lowercase.
    accountemail = models.CharField(db_column='accountEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    accountlv = models.CharField(db_column='accountLv', max_length=2)  # Field name made lowercase.
    state = models.CharField(max_length=1, blank=True, null=True)
    insertuser = models.CharField(db_column='insertUser', max_length=24, blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='updateUser', max_length=24, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.CharField(db_column='updateDate', max_length=21, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.CharField(db_column='insertDate', max_length=21)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_ADMINACCOUNT'


class TbInbody(models.Model):
    seq = models.IntegerField()
    membercode = models.CharField(max_length=14)
    weight = models.TextField()  # This field type is a guess.
    bonesheep = models.TextField(db_column='boneSheep')  # Field name made lowercase. This field type is a guess.
    fatsheep = models.TextField(db_column='fatSheep')  # Field name made lowercase. This field type is a guess.
    fatrate = models.TextField(db_column='fatRate')  # Field name made lowercase. This field type is a guess.
    insertdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'TB_INBODY'


class TbMeasurement(models.Model):
    membercode = models.CharField(max_length=14)
    rhr = models.CharField(max_length=2, blank=True, null=True)
    e_mhr = models.CharField(max_length=3, blank=True, null=True)
    vo2max = models.CharField(max_length=2, blank=True, null=True)
    mhr = models.CharField(max_length=3, blank=True, null=True)
    recovery = models.CharField(max_length=1, blank=True, null=True)
    frequency = models.CharField(max_length=2)
    intensity = models.CharField(max_length=6)
    target_time = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    wt = models.IntegerField()
    l1 = models.CharField(max_length=10)
    it = models.IntegerField()
    repeat = models.IntegerField()
    l2 = models.CharField(max_length=10)
    rt = models.IntegerField()
    ct = models.IntegerField()
    l3 = models.CharField(max_length=10)
    weight = models.CharField(max_length=3, blank=True, null=True)
    insertdate = models.DateField(unique=True)
    speed = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_MEASUREMENT'


class TbMember(models.Model):
    seq = models.IntegerField(primary_key=True)
    membercode = models.CharField(max_length=14)
    name = models.CharField(max_length=12)
    birthday = models.CharField(max_length=12)
    sex = models.CharField(max_length=2)
    height = models.CharField(max_length=3)
    weight = models.CharField(max_length=3)
    activility = models.CharField(max_length=2)
    insertdate = models.DateField()
    updatedate = models.CharField(max_length=50, blank=True, null=True)
    updateuser = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_MEMBER'


class TbRecord(models.Model):
    seq = models.IntegerField(primary_key=True)
    ptrymd = models.TextField(blank=True, null=True)  # This field type is a guess.
    ptprogram = models.TextField(blank=True, null=True)
    membercode = models.TextField(blank=True, null=True)  # This field type is a guess.
    ptrcomment = models.TextField(blank=True, null=True)
    ptrsessionf = models.CharField(blank=True, null=True)
    ptrsessionl = models.CharField(blank=True, null=True)
    ptrfrequency = models.CharField(blank=True, null=True)
    ptrintensity = models.CharField(blank=True, null=True)
    ptrtime = models.CharField(blank=True, null=True)
    ptrtype = models.CharField(blank=True, null=True)
    ptrmpcnt = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Record'


class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ZipCode(models.Model):
    zip_code = models.CharField(db_column='ZIP_CODE', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    s1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    s2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    s3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    s4 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'zip_code'
