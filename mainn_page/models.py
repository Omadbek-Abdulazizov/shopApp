from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category_name

class FruitCarts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    fruit_image = models.ImageField(upload_to='images/')
    fruit_likes = models.IntegerField(default=0)
    fruit_name = models.CharField(max_length=50)
    fruits_about = models.CharField(max_length=500)
    on_sale = models.BooleanField(default=False)
    old_price = models.IntegerField(default=0)
    fruits_price = models.IntegerField(default=0)

        
class Comments(models.Model):
    fruit_comment = models.ForeignKey(FruitCarts, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=50)
    text = models.TextField(max_length=800)
    comment_time = models.DateTimeField(auto_now_add=True)