from django.db import models


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
        ordering = ['-updatedate']


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


class TbAdminaccount(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    accountid = models.CharField(db_column='accountId', max_length=24)
    accountpw = models.CharField(db_column='accountPw', max_length=70)
    accountnm = models.CharField(db_column='accountNm', max_length=10)
    accountph = models.CharField(
        db_column='accountPh', max_length=15, blank=True, null=True)
    accountdpt = models.CharField(
        db_column='accountDpt', max_length=60, blank=True, null=True)
    accountemail = models.CharField(
        db_column='accountEmail', max_length=60, blank=True, null=True)
    accountlv = models.CharField(db_column='accountLv', max_length=2)
    state = models.CharField(max_length=1, blank=True, null=True)
    insertuser = models.CharField(
        db_column='insertUser', max_length=24, blank=True, null=True)
    updateuser = models.CharField(
        db_column='updateUser', max_length=24, blank=True, null=True)
    updatedate = models.CharField(
        db_column='updateDate', max_length=21, blank=True, null=True)
    insertdate = models.CharField(db_column='insertDate', max_length=21)

    class Meta:
        managed = False
        db_table = 'TB_ADMINACCOUNT'
