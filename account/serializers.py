from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Account, Transaction
from user.serializers import UserSerializer

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    account_id = serializers.IntegerField(required=False)
    class Meta:
        model = Transaction
        fields = ['account_id', 'operation', 'value', 'create_at']
        # extra_kwargs = {'balance': {'required': False}}

    def create(self, validated_data):
        account_id = validated_data.pop('account_id')
        validated_data['account'] = Account.objects.get(id=account_id)
        transaction = Transaction.objects.create(**validated_data)
        return transaction

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    transaction = TransactionSerializer(required=False,many=True)
    class Meta:
        model = Account
        fields = ['id', 'user', 'username', 'balance', 'transaction', 'create_at']
        extra_kwargs = {'balance': {'required': False}}

    def create(self, validated_data):
        account = Account.objects.create(**validated_data)
        return account

    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

