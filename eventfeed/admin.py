from django.contrib import admin

# Register your models here.
from eventfeed.models import Event


class EventAdmin(admin.ModelAdmin):
    save_as = True  # после добавления, текст остается
    save_on_top = True  # кнопка сохранения сверху


admin.site.register(Event, EventAdmin)
