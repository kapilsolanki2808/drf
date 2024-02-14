from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from snippets.serializers import UserSerializer,PasswordSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema, APIView,action
from rest_framework.schemas import AutoSchema
from rest_framework import request
from django.http import JsonResponse
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework import views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name="retrieve")
class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]
    # @method_decorator(login_required)
    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("invalid")
    
    def update(self, request,pk=None):
        objects = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(objects,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("invalid")

    def partial_update(self, request, pk=None):
        objects = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(objects,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("invalid")
    
    def destroy(self, request,pk):
        objects = get_object_or_404(self.queryset, pk=pk)
        objects.delete()
        return Response("deleted")
    




# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     # import pdb;pdb.set_trace()
#     @action(detail=True, methods=['post','get','patch','put','delete'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
    
#     @action(detail=True, methods=['get','delete'])
#     def delete_password(self, request,pk):
#         user = self.get_object()
#         # import pdb; pdb.set_trace()
#         # serializer = UserSerializer(user,request.data)
#         # if serializer.is_valid():
#         # print(view.reverse_action("set-password", args=["1"]))
#         user.set_unusable_password() # can not access password it set the password to LDAP 
#         # user.password = ''
#         user.save()
#         return Response({'status': 'password deleted'})
#         return Response("invalid")
    


    # @action(detail=False)
    # def recent_users(self, request):
    #     recent_users = User.objects.all().order_by('-last_login')

    #     page = self.paginate_queryset(recent_users)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(recent_users, many=True)
    #     return Response(serializer.data)




    






       
    


from rest_framework import mixins

class CreateListRetrieveViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()







# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action

# class UserViewSet(viewsets.ModelViewSet):
#     @action(detail=False, methods=['GET'])
#     def list_all_users(self, request):
#         objects = User.objects.all()
#         return Response(objects)
    
#     @action(detail=True, methods=['GET'])
#     def retrieve_user(self, request, pk=None):
#         try:
#             user_object = User.objects.get(pk=pk)
#             return Response(user_object)
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=404)










#######################################################
# from django.contrib.auth.models import User
# from snippets.serializers import UserSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
    

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)











class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        pass

@api_view(['GET'])
@schema(CustomAutoSchema())
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})




from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = User.objects.all()
            serializer = UserSerializer(instance, many=True)
            return Response(serializer.data)
        else:
            instance = User.objects.get(pk=pk)
            serializer = UserSerializer(instance)
            return Response(serializer.data)

    def post(self, request, format=None):
        return Response({'received data': request.data}, status=status.HTTP_201_CREATED)
    


    
class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filenafme, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
    
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import renderer_classes


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def simple(request):
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)
