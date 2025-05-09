from core.models import Product, Order, Customer
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "email", "company_name"]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source="customer", write_only=True
    )
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )

    class Meta:
        model = Order
        fields = [
            "product",
            "product_id",
            "customer",
            "customer_id",
            "quantity",
            "unit_price",
            "supplier",
        ]
