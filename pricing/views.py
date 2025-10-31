from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Vue pour lister tous les produits
def product_list(request):
    products = Product.objects.all().order_by('-updated_at')  # Récupère tous les produits triés
    return render(request, 'pricing/product_list.html', {'products': products})

# Vue pour afficher le détail d’un produit
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Récupère le produit ou affiche 404
    return render(request, 'pricing/product_detail.html', {'product': product})

# Vue pour ajouter un nouveau produit
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'pricing/product_form.html', {'form': form})

# Vue pour modifier un produit existant
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pricing/product_form.html', {'form': form})

# Vue pour supprimer un produit
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'pricing/product_confirm_delete.html', {'product': product})