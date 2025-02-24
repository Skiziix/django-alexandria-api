from django.urls import include, path

from rest_framework import routers

from .views import PublicLibrary

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('library/', PublicLibrary.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]