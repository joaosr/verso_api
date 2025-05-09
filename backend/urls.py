from django.urls import path, include
from rest_framework import routers
from core.views import ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"order", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
