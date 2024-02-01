from django.shortcuts import render, get_object_or_404, redirect
from .banks_models import Bank
from users.users_models import User
from .forms import BankForm

def add_banks(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save()
            return redirect('bank_detail', bank.id)
    else:
        form = BankForm()

    return render(request, 'banks/add_banks.html', {'form': form})
