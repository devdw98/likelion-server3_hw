from rest_framework import generics
from .serializers import HwSerializer
from .models import Hw
from django.shortcuts import get_object_or_404

class HwListAPIView(generics.ListCreateAPIView):
    queryset = Hw.objects.all()
    serializer_class = HwSerializer

class HwDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hw.objects.all()
    serializer_class = HwSerializer