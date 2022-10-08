from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Account, MonthlyPay
from api.network import Core
from .forms import TransferForm


# Create your views here.
@login_required
def index(request):
    user = Account.objects.get(user_id=request.user.id)
    return render(request, 'index.html',
                  {
                      'user': user,
                  })


@login_required
def profile(request, pk):
    resiever = Account.objects.get(pk=pk)
    sender = Account.objects.get(user_id=request.user.id)
    core = Core(sender.wallet.public_key, sender.wallet.secret_key)
    balance = core.balance
    balance_nft = core.balance_nft
    nfts = []
    for nft in balance_nft["balance"]:
        nfts.append({
            "amount": len(nft["tokens"]),
            "uri": nft["uri"]
        })
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            user_money_count = 123  # from api sender
            money_count = int(form.cleaned_data['money_count'])
            if money_count > user_money_count:
                print(f"You don't have {money_count} money")
            else:
                core.send_ruble(resiever.wallet.public_key, money_count)
    else:
        form = TransferForm()

    return render(request, 'profile.html', {'user': resiever,
                                            'form': form,
                                            'matic': balance["maticAmount"],
                                            'ruble': balance["coinsAmount"],
                                            'balance_nft': nfts,
                                            })


@login_required
def people_list(request):
    user_id = request.user.id
    people = Account.objects.all()
    return render(request, 'people_list.html', context={'people': people})


@csrf_exempt
def pay(request):
    users = Account.objects.all()
    if request.method == 'POST':
        public_address_receiver = request.POST.get('publicAddresReceiver')
        amount = request.POST.get('amount')
        user = Account.objects.get(user_id=request.user.id)
        public_sender_address = user.wallet.public_key
        secret_sender_address = user.wallet.secret_key
        core = Core(public_sender_address, secret_sender_address)
        core.send_ruble(public_address_receiver, amount)

        return render(request, 'manager.html', {'users': users})
    return render(request, 'manager.html', {'users': users})


def all_pay(request):
    admin_wallet = ('public_key', 'secret_key')
    core = Core(admin_wallet[0], admin_wallet[1])
    users = Account.objects.all()
    for user in users:
        mounfly_pay = MonthlyPay.objects.get(group=user.group)
        print(f"SEND FROM {admin_wallet[0]} TO {user.wallet.public_key} {mounfly_pay} {user.group}")
        # core.send_ruble(user.wallet.public_key, mounfly_pay)

    return render(request, 'admin_pay.html')
