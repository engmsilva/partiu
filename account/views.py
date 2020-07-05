from account.models import Account, Transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import viewsets
from account.serializers import AccountSerializer, TransactionSerializer
from .filter import AccountFilter

@authentication_classes([])
@permission_classes([])
class AccountViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AccountFilter

@authentication_classes([])
@permission_classes([])
class TransactionViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer