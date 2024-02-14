from rest_framework import serializers
from . models import Account
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
  url = serializers.CharField(source='get_absolute_url', read_only=True)
  groups = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  class Meta:
    model = Account
    fields = ['id', 'account_name', 'users', 'created', 'url', 'groups']
    # read_only_fields = ['account_name']
    # depth = 1

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user



class AccountSerializer1(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Account
      fields = ['url', 'id', 'account_name', 'users', 'created']
      


















# from model_serializer_app.models import *
# from model_serializer_app.serializer import *
# serializer = AccountSerializer()
# print(repr(serializer))