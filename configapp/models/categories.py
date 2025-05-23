from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('Type', related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
