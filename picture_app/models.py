from django.db import models


# Create your models here.
class Picture(models.Model):
    id = models.AutoField('id', primary_key=True)
    title = models.CharField('title', max_length=128, null=False)
    address = models.CharField('address', max_length=128, null=False)
    shot_time = models.DateTimeField('shot_time', auto_now_add=False, null=True)
    file = models.FileField('file', upload_to='picture_files', default='picture_files/default.png')
    upload_time = models.DateTimeField("create_time", auto_now_add=True)

    class Meta:
        db_table = 'pictures'