from django.shortcuts import render
from cowryRest.models import RandomUUID
from rest_framework import generics
from .serializers import RandomUUIDSerializer
# Create your views here.

class RandomUUIDListView(generics.ListAPIView):
    queryset = RandomUUID.objects.order_by('-time')
    serializer_class = RandomUUIDSerializer


class RandomUUIDDetail(generics.RetrieveAPIView):
    queryset = RandomUUID.objects.order_by('-time')
    serializer_class = RandomUUIDSerializer

