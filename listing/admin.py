from django.contrib import admin

# Register your models here.
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class meta:
        model = Stock


admin.site.register(Stock, StockAdmin)
