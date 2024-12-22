from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('new/',views.new_item, name='new' ),
    path('<int:pk>/',views.detail,name='detail'),
] 
