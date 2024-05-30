from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True, null = True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Item"
    
    def __str__(self):
        return self.name
