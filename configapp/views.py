from django.shortcuts import render, get_object_or_404, redirect
from configapp.models.categories import Category, Subcategory
from configapp.models.models import Transaction, Status, Type
from configapp.forms.Tranzactions_forms import TransactionForm
from configapp.forms.Forms import StatusForm, TypeForm, CategoryForm, SubcategoryForm
from django.utils.dateparse import parse_date



def dds_create_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print("CLEANED DATA:", form.cleaned_data)
            form.save()
            return redirect('dds_list')
        else:
            print("FORM ERRORS:", form.errors) 
            return render(request, 'Transaction/add_transaction.html', {'form': form}) 
    else:
        form = TransactionForm()
        return render(request, 'Transaction/add_transaction.html', {'form': form})

# Просмотр списка транзакций и фильтрация
def dds_list_view(request):
    records = Transaction.objects.select_related('status', 'category__type', 'subcategory').all()

    # Фильтры из GET-запроса
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    status = request.GET.get('status')
    type_ = request.GET.get('type')
    category = request.GET.get('category')
    subcategory = request.GET.get('subcategory')

    # Преобразование строковых значений дат в объекты даты
    if date_from:
        date_from = parse_date(date_from)
        if date_from:
            records = records.filter(date_created__gte=date_from)

    if date_to:
        date_to = parse_date(date_to)
        if date_to:
            records = records.filter(date_created__lte=date_to)

    
    if status:
        records = records.filter(status_id=status)
    if type_:
        records = records.filter(category__type_id=type_)
    if category:
        records = records.filter(category_id=category)
    if subcategory:
        records = records.filter(subcategory_id=subcategory)

    context = {
        'dds_list': records,
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'values': request.GET  # Возвращаем значения фильтров в контекст для их отображения в шаблоне
    }

    return render(request, 'Transaction/main_page.html', context)
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

    return render(request, 'Transaction/edit_transaction.html', {'form': form, 'transaction': transaction})

# Список статусов
def status_list_view(request):
    statuses = Status.objects.all()
    return render(request, 'Status/status_list.html', {'statuses': statuses})

# Создание статуса
def status_create_view(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных в базе
            return redirect('status_list')  # Перенаправление на страницу списка
    else:
        form = StatusForm()
    return render(request, 'Status/status_create.html', {'form': form})


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
    return render(request, 'Status/status_form.html', {'form': form})

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
    return render(request, 'Type/type_list.html', {'types': types})

# Создание типа
def type_create_view(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type_list')
    else:
        form = TypeForm()
    return render(request, 'Type/type_form.html', {'form': form})

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
    return render(request, 'Type/type_form.html', {'form': form})

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
    return render(request, 'Category/category_list.html', {'categories': categories})

# Создание категории
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'Category/category_form.html', {'form': form})

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
    return render(request, 'Category/category_form.html', {'form': form})

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
    return render(request, 'Subcategory/subcategory_list.html', {'subcategories': subcategories})

# Создание подкатегории
def subcategory_create_view(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm()
    return render(request, 'Subcategory/subcategory_form.html', {'form': form})

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
