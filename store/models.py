from django.db import models

class Category(models.Model):
    name = models.CharFiled(max_length=190)

    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharFiled(max_length=200)
    description = models.TextFiled()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title