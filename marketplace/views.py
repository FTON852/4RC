from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from marketplace.forms import WithdrawForm
from marketplace.models import Item


class HomeView(FormMixin, ListView):
    model = Item
    paginate_by = 9
    template_name = "item_list.html"
    context_object_name = 'items'
    form_class = WithdrawForm

    # success_url = "Заявка на вывод успешно создана"

    def get_success_url(self, **kwargs):
        return reverse('core:item_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        money_count = form.cleaned_data['money_count']
        # TODO проверка есть ли у чела баланс. Если есть то списываем и обновляем данные и выводим надпись.
        # Заявка на вывод {count} создана.
        # Недостаточно монет.
        print(money_count)
        return super().form_valid(form)


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
    context_object_name = 'item'
