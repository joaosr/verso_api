from rest_framework.test import APITestCase
from core.models import Product, Customer, Order
from rest_framework import status


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            company_name="ABC GmbH", email="abc@abc.de", password="testpass"
        )
        self.product = Product.objects.create(name="Product 1")
        self.client.login(username="abc@abc.de", password="testpass")

    def test_create_product(self):
        data = {"name": "Product2"}
        response = self.client.post("/product/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        data = {"name": "Product New Name"}
        response = self.client.put(f"/product/{self.product.pk}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Product New Name")

    def test_delete_product(self):
        response = self.client.delete(f"/product/{self.product.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            company_name="ABC GmbH", email="abc@abc.de", password="testpass"
        )
        self.product = Product.objects.create(name="Product 1")
        self.order = Order.objects.create(
            product=self.product,
            customer=self.customer,
            quantity=100,
            unit_price=370.7,
            supplier="BB Manufacture",
        )
        self.client.login(username="abc@abc.de", password="testpass")

    def test_create_order(self):
        data = {
            "product_id": self.product.pk,
            "customer_id": self.customer.pk,
            "quantity": 500,
            "unit_price": 50.6,
            "supplier": "BB Ko",
        }
        response = self.client.post("/order/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_update_order(self):
        data = {
            "product_id": self.product.pk,
            "customer_id": self.customer.pk,
            "quantity": 400,
            "unit_price": 307.6,
            "supplier": "AA Manufacture",
        }
        response = self.client.put(f"/order/{self.order.pk}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.quantity, 400)
        self.assertEqual(self.order.unit_price, 307.6)
        self.assertEqual(self.order.supplier, "AA Manufacture")

    def test_delete_order(self):
        response = self.client.delete(f"/order/{self.order.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())
