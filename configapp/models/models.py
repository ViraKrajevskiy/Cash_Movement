from django.db import models
from django.core.exceptions import ValidationError
from configapp.models import Category, Subcategory


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('business', 'Бизнес'),
        ('personal', 'Личное'),
        ('tax', 'Налог'),
    ]

    TYPE_CHOICES = [
        ('deposit', 'Пополнение'),
        ('withdrawal', 'Списание'),
    ]

    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    category = models.ForeignKey('configapp.Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('configapp.Subcategory', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date_created} | {self.status.name} | {self.type.name} | {self.amount}₽"

    def clean(self):
        # Обязательные поля
        if not self.amount:
            raise ValidationError({'amount': 'Поле "Сумма" обязательно для заполнения.'})
        if not self.type:
            raise ValidationError({'type': 'Поле "Тип" обязательно для заполнения.'})
        if not self.category:
            raise ValidationError({'category': 'Поле "Категория" обязательно для заполнения.'})
        if not self.subcategory:
            raise ValidationError({'subcategory': 'Поле "Подкатегория" обязательно для заполнения.'})

        # Проверка соответствия категории выбранному типу
        if self.category.type != self.type:
            raise ValidationError({'category': 'Выбранная категория не соответствует выбранному типу.'})

        # Проверка соответствия подкатегории выбранной категории
        if self.subcategory.category != self.category:
            raise ValidationError({'subcategory': 'Выбранная подкатегория не принадлежит выбранной категории.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # вызывает clean()
        super().save(*args, **kwargs)