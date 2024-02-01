from django.shortcuts import render, get_object_or_404
from .banks_models import Bank
from users.users_models import User

def bank_list(request):
    banks = Bank.objects.all()
    return render(request, 'banks/bank_list.html', {'banks': banks})

def bank_detail(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    return render(request, 'banks/bank_detail.html', {'bank': bank})
