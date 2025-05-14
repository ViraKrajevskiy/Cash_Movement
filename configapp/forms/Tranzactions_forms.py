from django import forms
from configapp.models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'status': forms.Select(attrs={"class": "form-control"}),
            'type': forms.Select(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'subcategory': forms.Select(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Введите сумму"}),
            'comment': forms.Textarea(attrs={"class": "form-control", "placeholder": "Комментарий...", "rows": 3}),
        }

    def clean_category(self):
        category = self.cleaned_data.get('category')
        transaction_type = self.cleaned_data.get('type')
        if category and transaction_type and category.type != transaction_type:
            raise forms.ValidationError('Выбранная категория не соответствует выбранному типу.')
        return category

    def clean_subcategory(self):
        subcategory = self.cleaned_data.get('subcategory')
        category = self.cleaned_data.get('category')
        if subcategory and category and subcategory.category != category:
            raise forms.ValidationError('Выбранная подкатегория не принадлежит выбранной категории.')
        return subcategory
        