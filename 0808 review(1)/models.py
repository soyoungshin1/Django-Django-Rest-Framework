from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class WineReview(models.Model):
    #cascade = wine 이 삭제되면 review 다 삭제됨.
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )

    def __str__(self):
        return self.title
