from rest_framework import generics, filters

from network.models import SalesNetwork
from network.serializers import SalesNetworkSerializer
from users.permissions import IsActive


class SalesNetworkListApiView(generics.ListAPIView):
    """Просмотр участников сетей продаж, которые являются также поставщиками"""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["country"]
    permission_classes = (IsActive,)


class SalesNetworkCreateApiView(generics.CreateAPIView):
    """Создание нового участника сети продаж"""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = (IsActive,)


class SalesNetworkRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр информации о конкретном участнике сети продаж"""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = (IsActive,)


class SalesNetworkUpdateApiView(generics.UpdateAPIView):
    """Изменение информации о конкретном участнике сети продаж"""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = (IsActive,)


class SalesNetworkDestroyApiView(generics.DestroyAPIView):
    """Удаление участника сети продаж"""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = (IsActive,)
