from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BookModel(models.Model):
    title = models.CharField(max_length=400)
    price = models.IntegerField()
    publish_date = models.DateField(null=True)
    author = models.ManyToManyField(AuthorModel, null=True)

    def __str__(self):
        return self.title
