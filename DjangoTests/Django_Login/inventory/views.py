from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django_pandas.io import read_frame
import plotly
import plotly.express as px
import json
from .models import Inventory
from .forms import AddInventoryForm


# Create your views here.
@login_required
def inventory(request):
    inventories = Inventory.objects.all()
    context = {
        'title': 'Inventory List',
        'inventories': inventories,
    }
    return render(request, 'inventory/inventory_list.html', context)


@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'title': 'Product View',
        'inventory': inventory,
    }
    return render(request, 'inventory/per_product.html', context)


@login_required
def add_product(request):
    if request.method == 'POST':
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            new_inventory.save()
            messages.success(request, "Successfully added the product")
            return redirect('/inventory/')
    else:
        add_form = AddInventoryForm()

    context = {
        'title': 'Add Product',
        'form': add_form,
    }
    return render(request, 'inventory/inventory_add.html', context)


@login_required
def delete_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    messages.warning(request, "Successfully deleted the product")

    return redirect('/inventory/')


@login_required
def update_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        # inherited from add form since they look the same
        update_form = AddInventoryForm(data=request.POST)
        if update_form.is_valid():
            inventory.name = update_form.data['name']
            inventory.quantity_in_stock = update_form.data['quantity_in_stock']
            inventory.cost_per_item = update_form.data['cost_per_item']
            inventory.quantity_sold = update_form.data['quantity_sold']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantity_sold)
            inventory.save()
            messages.info(request, "Successfully updated the product")
            return redirect(f'/inventory/product/{pk}')
    else:
        update_form = AddInventoryForm(instance=inventory)

    context = {
        'title': 'Update Product',
        'form': update_form,
    }
    return render(request, 'inventory/inventory_update.html', context)


@login_required
def dashboard(request):
    inventories = Inventory.objects.all()

    # data frame
    df = read_frame(inventories)

    # graph
    sales_graph = df.groupby(by="last_sales_date", as_index=False, sort=False)['sales'].sum()
    sales_graph = px.line(sales_graph, x=sales_graph.last_sales_date, y=sales_graph.sales, title='Sales Trend')
    sales_graph = json.dumps(sales_graph, cls=plotly.utils.PlotlyJSONEncoder)

    # another graph
    best_performing_product_df = df.groupby(by='name').sum().sort_values(by='quantity_sold')
    best_performing_product = px.bar(best_performing_product_df, x=best_performing_product_df.index,
                                     y=best_performing_product_df.quantity_sold, title='Best Performing Product')
    best_performing_product = json.dumps(best_performing_product, cls=plotly.utils.PlotlyJSONEncoder)

    # graph 3
    most_product_in_stock_df = df.groupby(by='name').sum().sort_values(by='quantity_in_stock')
    most_product_in_stock = px.pie(most_product_in_stock_df, names=most_product_in_stock_df.index,
                                   values=most_product_in_stock_df.quantity_in_stock, title='Most Product In Stock')
    most_product_in_stock = json.dumps(most_product_in_stock, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'sales_graph': sales_graph,
        'best_performing_product': best_performing_product,
        'most_product_in_stock': most_product_in_stock,
    }
    return render(request, 'inventory/dashboard.html', context)
