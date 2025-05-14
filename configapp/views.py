from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect,render

from configapp.forms.Tranzactions_forms import TransactionForm
from configapp.models.models import Transaction

def dds_list_view(request):
    records = Transaction.objects.select_related('status', 'category__type', 'subcategory').all()
    return render(request, 'main_page.html', {'dds_list': records})


def dds_delete_view(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == "POST":
        transaction.delete()
        return redirect('dds_list')
    return render(request, 'confirm_delete.html', {'transaction': transaction})


def dds_edit_view(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('dds_list')  # Перенаправляем на список транзакций
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'dds_edit.html', {'form': form, 'transaction': transaction})