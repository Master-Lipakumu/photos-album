from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    image = models.ImageField(upload_to='photos_album')
    date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    def __str__(self):
        return self.title