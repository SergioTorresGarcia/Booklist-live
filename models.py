from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    publishing_year = models.IntegerField(null=True)
    ISBN_number = models.IntegerField()
    number_of_pages = models.PositiveIntegerField(null=True)
    language = models.CharField(max_length=32)
    book_cover = models.ImageField(upload_to="../media/", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
