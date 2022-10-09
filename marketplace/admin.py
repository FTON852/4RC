from django.contrib import admin

# Register your models here.
from marketplace.models import Item


class ProductAdmin(admin.ModelAdmin):
    save_as = True  # после добавления, текст остается
    save_on_top = True  # кнопка сохранения сверху


admin.site.register(Item, ProductAdmin)
