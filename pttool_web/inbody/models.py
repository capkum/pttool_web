from django.db import models


class TbInbody(models.Model):
    seq = models.IntegerField()
    membercode = models.CharField(max_length=14)
    weight = models.TextField()
    bonesheep = models.TextField()
    fatsheep = models.TextField()
    fatrate = models.TextField()
    insertdate = models.DateField()

    class Meta:
        db_table = 'TB_INBODY'
        managed = True
