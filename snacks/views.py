from django.shortcuts import render
from .models import Snack
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer
from .permissions import IsOwnerOrReadOnly

class SnackList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
