from django.shortcuts import render
from listing.models import Stock
from django.db.models import Q


def search_stock_list_view(request):
    query = request.GET.get('q')
    print(request.GET)
    if query is not None:
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query))

        queryset = Stock.objects.filter(lookup).distinct()
    else:
        queryset = Stock.objects.none()
    context = {
        'Object_list': queryset
    }
    return render(request, 'search/search_view.html', context)
