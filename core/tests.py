from django.test import TestCase
from core.models import Product, Customer, Order


class ProductTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Product 1")

    def test_create_product(self):
        self.assertIsNotNone(self.product.id)

    def test_update_product(self):
        self.product.name = "Product New Name"
        self.product.save()
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.name, "Product New Name")

    def test_delete_product(self):
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)


class OrderTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            company_name="ABC GmbH", email="abc@abc.de"
        )
        self.product = Product.objects.create(name="Product 1")
        self.order = Order.objects.create(
            product=self.product,
            customer=self.customer,
            quantity=100,
            unit_price=370.7,
            supplier="BB Manufacture",
        )

    def test_create_order(self):
        self.assertIsNotNone(self.order.id)

    def test_update_order(self):
        self.order.quantity = 200
        self.order.unit_price = 400.0
        self.order.save()
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.quantity, 200)
        self.assertEqual(order.unit_price, 400.0)

    def test_delete_order(self):
        order_id = self.order.id
        self.order.delete()
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id=order_id)
