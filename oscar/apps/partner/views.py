# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from oscar.apps.catalogue.models import Product
from oscar.apps.partner.models import StockRecord
from oscar.apps.partner.strategy import Selector
from .forms import MyForm

# class MyFormView(View):
#     form_class = MyForm
#     template_name = 'partner/partner_form.html'
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk","")
#         obj = Product.objects.get(id=pk)
#         strategy = Selector().strategy()
#         stock = strategy.fetch_for_product(obj)
#         data = {'product_quantity' : obj.attr.MinQuantity}
#         form = self.form_class(initial=data)
#         return render(request, self.template_name, {'form': form,'supplier_name':stock.stockrecord.partner.name, 'product_name':obj.title })
#
#     def post(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", "")
#         obj = Product.objects.get(id=pk)
#         strategy = Selector().strategy()
#         stock = strategy.fetch_for_product(obj)
#         data = {'product_quantity': obj.attr.MinQuantity}
#         form = self.form_class(request.POST, request.FILES,initial=data)
#
#         if form.is_valid():
#             # <process form cleaned data>
#             formobj = form.save(commit=False)
#             formobj.product_name = obj.title
#             formobj.product_supplier = stock.stockrecord.partner.name
#             formobj.save()
#             return HttpResponseRedirect('/success/')
#
#         return render(request, self.template_name, {'form': form, 'supplier_name':stock.stockrecord.partner.name, 'product_name':obj.title})


def form_view(request,pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        obj = Product.objects.get(id=pk)
        strategy = Selector().strategy()
        stock = strategy.fetch_for_product(obj)
        # data = {'product_quantity': obj.attr.MinQuantity}
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            formobj = form.save(commit=False)
            formobj.product_name = obj.title
            formobj.product_supplier = stock.stockrecord.partner.name
            formobj.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        obj = Product.objects.get(id=pk)
        strategy = Selector().strategy()
        stock = strategy.fetch_for_product(obj)
        data = {'product_quantity': obj.attr.MinQuantity}
        form = MyForm(initial=data)

    return render(request, 'partner/partner_form.html', {'form': form,'supplier_name':stock.stockrecord.partner.name,
                                                         'product_name':obj.title})