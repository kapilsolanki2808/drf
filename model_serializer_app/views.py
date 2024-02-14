from django.shortcuts import render
from .serializer import CreateUserSerializer,AccountSerializer1
from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Account
from rest_framework import request
class CreateListRetrieveViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,viewsets.GenericViewSet,
                                mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

class HyperLinkedTest(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer1

        