from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # 총 자릿수 6 자리, 소수점 이하 2자리