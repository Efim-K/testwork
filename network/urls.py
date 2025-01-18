from django.urls import path

from network.apps import NetworkConfig
from network.views import (
    SalesNetworkListApiView,
    SalesNetworkCreateApiView,
    SalesNetworkRetrieveApiView,
    SalesNetworkUpdateApiView,
    SalesNetworkDestroyApiView,
)

app_name = NetworkConfig.name

urlpatterns = [
    path("network/", SalesNetworkListApiView.as_view(), name="network-list"),
    path("network/create/", SalesNetworkCreateApiView.as_view(), name="network-create"),
    path(
        "network/<int:pk>/",
        SalesNetworkRetrieveApiView.as_view(),
        name="network-retrieve",
    ),
    path(
        "network/<int:pk>/update/",
        SalesNetworkUpdateApiView.as_view(),
        name="network-update",
    ),
    path(
        "network/<int:pk>/delete/",
        SalesNetworkDestroyApiView.as_view(),
        name="network-delete",
    ),
]
