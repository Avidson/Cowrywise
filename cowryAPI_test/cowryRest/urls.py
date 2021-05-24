from django.urls import path, include
from django.contrib import admin
from cowryRest.views import RandomUUIDListView, RandomUUIDDetail
from django.conf import settings 


app_name = 'cowryRest'

urlpatterns = [
    path('objects/', RandomUUIDListView.as_view(), name="objects"),
    path('objects/<pk>/', RandomUUIDDetail.as_view(), name = 'objects_details')
]
