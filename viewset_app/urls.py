from django.urls import path
from viewset_app import views
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer


urlpatterns = [
    # path('userlist/', views.UserViewSet.as_view({'get': 'list'})),
    path('view/', views.view),
    path('simple/', views.simple),
    # path('users/', views.ExampleView.as_view(), name='user-list'),  # For listing all users
    # path('users/<int:pk>/', views.ExampleView.as_view()), 


    # path('users/', views.UserList.as_view(), name="user-list")
   
    path('users/', views.UserViewSet.as_view({'post': 'retrieve', 'get': 'list'})),
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve','patch':'partial_update','put':'update'})),

]

from viewset_app.views import UserViewSet,CreateListRetrieveViewSet,ExampleView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
router.register(r'mixin', CreateListRetrieveViewSet, basename='CreateListRetrieveViewSet')
# router.register(r'ExampleView', ExampleView.as_view(), basename='ExampleView')  
# urlpatterns += router.urls