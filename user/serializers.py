from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'profile']
        extra_kwargs = {'username': {'required': False}}

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        print(validated_data)
        user = User.objects.create_user(**validated_data, is_staff=True)
        Profile.objects.create(user=user, **profile)
        return user

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        Profile.objects.filter(user=instance).update(**profile)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

