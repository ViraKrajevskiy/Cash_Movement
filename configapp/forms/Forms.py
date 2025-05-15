from django import forms
from configapp.models import Status, Subcategory, Category, Type


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название статуса обязательно для заполнения.')
        return name



class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название типа обязательно для заполнения.')
        return name




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название категории обязательно для заполнения.')
        return name

    def clean(self):
        cleaned_data = super().clean()
        category_type = cleaned_data.get('type')

        # Проверка, чтобы категория была привязана к типу
        if not category_type:
            raise forms.ValidationError({'type': 'Выберите тип категории.'})

        return cleaned_data




class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название подкатегории обязательно для заполнения.')
        return name

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')

        # Проверка, чтобы подкатегория была привязана к категории
        if not category:
            raise forms.ValidationError({'category': 'Выберите категорию для подкатегории.'})

        return cleaned_data

