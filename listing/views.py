from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from .models import Stock, Order


# Create your views here.


class ClassListView(ListView):
    queryset = Stock.objects.all()
    template_name = 'listing/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClassListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def stock_list_view(request):
    queryset = Stock.objects.all()
    context = {
        'Object_list': queryset
    }
    return render(request, 'listing/stock_list.html', context)


def stock_detail_view(request, id):
    obj = Stock.objects.get(id=id)
    if obj is None:
        raise Http404
    context = {
        'obj': obj
    }
    return render(request, 'listing/stock_detail.html', context)


def save_order(request):
    if request.method == "POST":
        quantity = request.POST['quantity']
        # order = Order.objects.create(quantity)
    return render(request, 'listing/order_info.html')