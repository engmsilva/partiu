from .models import Account
from django_filters import rest_framework as filters, DateFromToRangeFilter

class AccountFilter(filters.FilterSet):
    transaction__create_at = DateFromToRangeFilter()

    class Meta:
        model = Account
        distinct = True
        fields = ['user__username', 'transaction__create_at' ]