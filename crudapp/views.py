from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .data_forms import ItemForm # অথবা আপনার forms.py থেকে

# 1. Read (সব ডেটা দেখানো)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})

# 2. Create (নতুন ডেটা যোগ করা)
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'core/item_form.html', {'form': form})

# 3. Update (existing ডেটা এডিট করা)
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'core/item_form.html', {'form': form})

# 4. Delete (ডেটা মুছে ফেলা)
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'core/item_confirm_delete.html', {'item': item})