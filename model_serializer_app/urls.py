from django.urls import path
from model_serializer_app import views
from django.contrib.auth.models import User
from .views import CreateListRetrieveViewSet,HyperLinkedTest

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
#   path('HyperLinkedTest/',views.HyperLinkedTest.as_view({'get':'list','post':'create'}),name='HyperLinkedTest-detail'),
#   path('HyperLinkedTest/<int:pk>',views.HyperLinkedTest.as_view({'get':'retrieve'}),name='HyperLinkedTest-detail')
] # aboive url is not working properly

router = DefaultRouter()
router.register(r'list_single_object', CreateListRetrieveViewSet, basename='create')
router.register(r'HyperLinkedTest', HyperLinkedTest)  
urlpatterns += router.urls