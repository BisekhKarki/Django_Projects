from home.views import index,people,login, PersonApi,PeopleViewSet

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people',PeopleViewSet, basename='people')
urlpatterns = router.urls



urlpatterns = [

    path('', include(router.urls)),
    path('index/', index),
    path('person/', people),
    path('login/', login),
    path('persons/',PersonApi.as_view() ),
]
