from django.db import models
from decimal import Decimal

class Review(models.Model):
    title = models.CharField(max_length=100)
    wine_name = models.CharField(max_length=250)
    
    #와인테이블에 FK 관계이고, on_delete 관계 표현
    #wine = models.ForeignKey(Wine, on_delete=models.CASCADE) #작성자

    RATING_CHOICES = [
        (Decimal('1.0'), '1.0'),
        (Decimal('1.5'), '1.5'),
        (Decimal('2.0'), '2.0'),
        (Decimal('2.5'), '2.5'),
        (Decimal('3.0'), '3.0'),
        (Decimal('3.5'), '3.5'),
        (Decimal('4.0'), '4.0'),
        (Decimal('4.5'), '4.5'),
        (Decimal('5.0'), '5.0')
    ]
    
    rating = models.DecimalField(
        max_digits=2, #최대 자릿수
        decimal_places=1, #소수점 자리수
        choices=RATING_CHOICES
    )
    
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return self.title