from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("quickstart.urls")),
    path("snippet/",include("snippets.urls")),
    path("viewset_app/",include("viewset_app.urls")),
    path("serializer/",include("serializer_app.urls")),
    path("model/serializer/",include("model_serializer_app.urls")),
]