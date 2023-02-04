# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# views.py
from django.shortcuts import render
from .models import Transaction

def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'personal_finance/transaction_list.html', context)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transaction_list, name='transaction_list'),
]
