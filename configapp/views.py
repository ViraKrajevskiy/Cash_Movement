from django.shortcuts import render, get_object_or_404, redirect
from configapp.models.categories import *
from configapp.models.models import *
from configapp.forms.Tranzactions_forms import TransactionForm
from configapp.forms.Forms import StatusForm, TypeForm, CategoryForm, SubcategoryForm

# Создание транзакции
def dds_create_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds_list')  # Перенаправление на страницу списка транзакций
    else:
        form = TransactionForm()

    return render(request, 'add_transaction.html', {'form': form})

# Просмотр списка транзакций
def dds_list_view(request):
    records = Transaction.objects.select_related('status', 'category__type', 'subcategory').all()
    return render(request, 'main_page.html', {'dds_list': records})

# Удаление транзакции
def dds_delete_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
        return redirect('dds_list')
    return render(request, 'confirm_delete.html', {'transaction': transaction})

# Редактирование транзакции
def dds_edit_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dds_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'dds_edit.html', {'form': form, 'transaction': transaction})

# Список статусов
def status_list_view(request):
    statuses = Status.objects.all()
    return render(request, 'status_list.html', {'statuses': statuses})

# Создание статуса
def status_create_view(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm()
    return render(request, 'status_form.html', {'form': form})

# Редактирование статуса
def status_edit_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'status_form.html', {'form': form})

# Удаление статуса
def status_delete_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('status_list')
    return render(request, 'confirm_delete.html', {'object': status})

# Список типов
def type_list_view(request):
    types = Type.objects.all()
    return render(request, 'type_list.html', {'types': types})

# Создание типа
def type_create_view(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type_list')
    else:
        form = TypeForm()
    return render(request, 'type_form.html', {'form': form})

# Редактирование типа
def type_edit_view(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            return redirect('type_list')
    else:
        form = TypeForm(instance=type_obj)
    return render(request, 'type_form.html', {'form': form})

# Удаление типа
def type_delete_view(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        type_obj.delete()
        return redirect('type_list')
    return render(request, 'confirm_delete.html', {'object': type_obj})

# Список категорий
def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# Создание категории
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

# Редактирование категории
def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

# Удаление категории
def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'confirm_delete.html', {'object': category})

# Список подкатегорий
def subcategory_list_view(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'subcategory_list.html', {'subcategories': subcategories})

# Создание подкатегории
def subcategory_create_view(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm()
    return render(request, 'subcategory_form.html', {'form': form})

# Редактирование подкатегории
def subcategory_edit_view(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'subcategory_form.html', {'form': form})

# Удаление подкатегории
def subcategory_delete_view(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('subcategory_list')
    return render(request, 'confirm_delete.html', {'object': subcategory})
