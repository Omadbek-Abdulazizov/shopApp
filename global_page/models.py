from django.db import models

# Create your models here.
class PageGlobalVeraibles(models.Model):
    image = models.ImageField(upload_to='images/', editable='True')
class PageTextVeraibles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    def __str__(self) -> str:
        return self.title