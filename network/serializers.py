from rest_framework.serializers import ModelSerializer

from network.models import SalesNetwork
from network.validators import SalesNetworkValidators


class SalesNetworkSerializer(ModelSerializer):
    """Сериализатор для модели SalesNetwork"""

    class Meta:
        model = SalesNetwork
        fields = "__all__"
        read_only_fields = ["debt"]
        validators = [SalesNetworkValidators()]
