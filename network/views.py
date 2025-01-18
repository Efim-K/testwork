from rest_framework import generics, filters

from network.models import SalesNetwork
from network.serializers import SalesNetworkSerializer


class SalesNetworkListApiView(generics.ListAPIView):
    """Просмотр участников сетей продаж, которые являются также поставщиками"""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class SalesNetworkCreateApiView(generics.CreateAPIView):
    """Создание нового участника сети продаж"""
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр информации о конкретном участнике сети продаж"""
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkUpdateApiView(generics.UpdateAPIView):
    """Изменение информации о конкретном участнике сети продаж"""
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkDestroyApiView(generics.DestroyAPIView):
    """Удаление участника сети продаж"""
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
