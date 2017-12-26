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
    insertdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'TB_MEMBER'
        managed = True


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
    insertdate = models.DateTimeField(auto_now_add=True, unique=True)
    speed = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'TB_MEASUREMENT'
        managed = True


class TbAdminaccount(models.Model):
    seq = models.IntegerField(primary_key=True)
    accountid = models.CharField(max_length=24)
    accountpw = models.CharField(max_length=70)
    accountnm = models.CharField(max_length=10)
    accountph = models.CharField(max_length=15, blank=True, null=True)
    accountdpt = models.CharField(max_length=60, blank=True, null=True)
    accountemail = models.CharField(max_length=60, blank=True, null=True)
    accountlv = models.CharField(max_length=2)
    state = models.CharField(max_length=1, blank=True, null=True)
    insertuser = models.CharField(max_length=24, blank=True, null=True)
    updateuser = models.CharField(max_length=24, blank=True, null=True)
    updatedate = models.DateField(
        auto_now=True, max_length=21, blank=True, null=True)
    insertdate = models.DateField(auto_now_add=True, max_length=21)

    class Meta:
        db_table = 'TB_ADMINACCOUNT'
        managed = True
