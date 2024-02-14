from django.urls import path
from serializer_app import views
from django.contrib.auth.models import User
from serializer_app.serializer import CommentSerializer
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('view/', views.CommentAPIView.as_view()),
    path('view/<int:pk>/', views.CommentAPIView.as_view()),
    path('validate/', views.Validate.as_view()),
    path('validate/<int:pk>/', views.Validate.as_view()),
 
]




# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'mixin', CreateListRetrieveViewSet, basename='CreateListRetrieveViewSet')
# # router.register(r'ExampleView', ExampleView.as_view(), basename='ExampleView')  
# urlpatterns += router.urls