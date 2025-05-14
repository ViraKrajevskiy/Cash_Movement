from django import forms
from configapp.models.models import Transaction, Status, Type, Category, Subcategory

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment']  # Убираем 'date_created'

    # Валидация поля 'amount'
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError('Сумма должна быть положительным числом.')
        return amount

    # Валидация поля 'category' в зависимости от выбранного 'type'
    def clean_category(self):
        category = self.cleaned_data.get('category')
        transaction_type = self.cleaned_data.get('type')
        if category and transaction_type:
            if category.type != transaction_type:
                raise forms.ValidationError('Выбранная категория не соответствует выбранному типу.')
        return category

    # Валидация поля 'subcategory' в зависимости от выбранной 'category'
    def clean_subcategory(self):
        subcategory = self.cleaned_data.get('subcategory')
        category = self.cleaned_data.get('category')
        if subcategory and category:
            if subcategory.category != category:
                raise forms.ValidationError('Выбранная подкатегория не принадлежит выбранной категории.')
        return subcategory
