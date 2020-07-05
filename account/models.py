from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.FloatField(max_length=30, default=0, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def username(self):
        return self.user.username

class Transaction(models.Model):
    account = models.ForeignKey(Account, related_name='transaction', on_delete=models.CASCADE)
    operation = models.CharField(max_length=30)
    value = models.FloatField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        account = Account.objects.get(pk=self.account.pk)
        balance = getattr(account, 'balance')
        if self.operation == 'debit':
            account.balance = balance - self.value
        if self.operation == 'credit':
            account.balance = balance + self.value
        account.save()
        super().save(*args, **kwargs)