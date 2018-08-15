from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    month = models.IntegerField(
        verbose_name="月份",
        default=12,
        db_column="my_month"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="登记日期"
    )
    last_update = models.DateField(
        auto_now=True
    )
    is_used = models.BooleanField(
        default=True,
        verbose_name="是否在用"
    )
    def __str__(self):
            return self.name+str(self.month)
    class Meta:
        verbose_name = "水果类",
        db_table = "guoguo"