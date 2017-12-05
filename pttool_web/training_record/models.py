from django.db import models


class TbRecord(models.Model):
    seq = models.IntegerField(primary_key=True)
    ptrymd = models.TextField(max_length=12, blank=True, null=True)
    ptprogram = models.TextField(blank=True, null=True)
    membercode = models.TextField(blank=True, null=True)
    ptrcomment = models.TextField(blank=True, null=True)
    ptrsessionf = models.CharField(max_length=2, blank=True, null=True)
    ptrsessionl = models.CharField(max_length=2, blank=True, null=True)
    ptrfrequency = models.CharField(max_length=1, blank=True, null=True)
    ptrintensity = models.CharField(max_length=3, blank=True, null=True)
    ptrtime = models.CharField(max_length=3, blank=True, null=True)
    ptrtype = models.CharField(max_length=12, blank=True, null=True)
    ptrmpcnt = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'TB_RECORD'
        managed = True
