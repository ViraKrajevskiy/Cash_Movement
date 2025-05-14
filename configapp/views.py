from django.shortcuts import render, get_object_or_404, redirect
from configapp.models.categories import *
from configapp.models.models import *
from configapp.forms.Tranzactions_forms import TransactionForm

def dds_list_view(request):
    records = Transaction.objects.select_related('status', 'category__type', 'subcategory').all()
    return render(request, 'main_page.html', {'dds_list': records})

def dds_delete_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
        return redirect('dds_list')
    return render(request, 'confirm_delete.html', {'transaction': transaction})

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
