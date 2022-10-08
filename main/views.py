from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Account
from .forms import TransferForm

# Create your views here.
@login_required
def index(request):
    user = Account.objects.get(user_id=request.user.id)
    return render(request, 'index.html', {'user': user})


@login_required
def profile(request, pk):
    resiever = Account.objects.get(pk=pk)
    sender = Account.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            user_money_count = 123 # from api sender
            money_count = form.cleaned_data['money_count']
            if int(money_count) > user_money_count:
                print(f"You don't have {money_count} money")
            else:
                # транзакция с переводом снять у отправителя, положить получателю
                pass
        return render(request, 'profile.html', {'user': resiever, 'form': form})

    else:
        form = TransferForm()
    return render(request, 'profile.html', {'user': resiever, 'form': form})


@login_required
def people_list(request):
    user_id = request.user.id
    people = Account.objects.all()
    return render(request, 'people_list.html', context={'people': people})
