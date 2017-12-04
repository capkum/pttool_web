from django.db import models


class TbInbody(models.Model):
    seq = models.IntegerField()
    membercode = models.CharField(max_length=14)
    weight = models.TextField()  # This field type is a guess.
    # Field name made lowercase. This field type is a guess.
    bonesheep = models.TextField(db_column='boneSheep')
    # Field name made lowercase. This field type is a guess.
    fatsheep = models.TextField(db_column='fatSheep')
    # Field name made lowercase. This field type is a guess.
    fatrate = models.TextField(db_column='fatRate')
    insertdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'TB_INBODY'
