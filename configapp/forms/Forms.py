from django import forms
from configapp.models import Status, Subcategory, Category, Type


class StatusForm(forms.Form):
    name = forms.CharField(
        label='Название статуса',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название статуса обязательно для заполнения.')
        return name



class TypeForm(forms.Form):
    name = forms.CharField(
        label='Название типа',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название типа обязательно для заполнения.')
        return name




class CategoryForm(forms.Form):
    name = forms.CharField(
        label='Название категории',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    type = forms.ModelChoiceField(
        label='Тип',
        queryset=Type.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название категории обязательно для заполнения.')
        return name



class SubcategoryForm(forms.Form):
    name = forms.CharField(
        label='Название подкатегории',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название подкатегории обязательно для заполнения.')
        return name
        