from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardViewSet
from django.contrib import admin


router = DefaultRouter()

urlpatterns = [
    path('cards', CardViewSet.as_view({'get':'list','post':'create'}), name='cards' )

]
