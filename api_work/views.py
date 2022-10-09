import json

from django.http import HttpResponse
from api.network import Core


def balance(request, public_key):
    core = Core(public_key)
    try:
        data = core.balance
    except Exception:
        data = {
            "success": False
        }
    return HttpResponse(json.dumps(data), content_type='application/json')


def balance_nft(request, public_key):
    core = Core(public_key)
    try:
        balance_nft = core.balance_nft
        nfts = []
        for nft in balance_nft["balance"]:
            nfts.append({
                "amount": len(nft["tokens"]),
                "uri": nft["uri"]
            })
        data = nfts
    except Exception:
        data = {
            "success": False
        }
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_nft(request, id):
    core = Core()
    try:
        data = core.get_nft(id)
    except Exception:
        data = {
            "success": False
        }
    return HttpResponse(json.dumps(data), content_type='application/json')


def transactions_history(request, public_key):
    core = Core(public_key)
    try:
        data = core.transactions_history()

    except Exception:
        data = {
            "success": False
        }
    return HttpResponse(json.dumps(data), content_type='application/json')
