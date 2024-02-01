from django.shortcuts import render, get_object_or_404, redirect
from .users_models import User
from banks.banks_models import Bank
from .forms import UserForm

def add_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', user.id)
    else:
        form = UserForm()

    return render(request, 'users/add_users.html', {'form': form})
