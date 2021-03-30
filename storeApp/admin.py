from django.contrib import admin
from .models import Category, Stock
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']

# Register your models here.
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)