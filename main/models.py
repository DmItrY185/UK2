from django.db import models


class Code(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='Код')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'code'

    def __str__(self):
        return self.code
