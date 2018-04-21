from django.shortcuts import render, get_object_or_404
from .models import Debit, Credit

# Create your views here.

def index(request):
    debit_list = Debit.objects.order_by('-date')
    credit_list = Credit.objects.order_by('date')
    context = {
        'debit_list':debit_list,
        'credit_list':credit_list
    }
    return render(request, 'checking/index.html', context)