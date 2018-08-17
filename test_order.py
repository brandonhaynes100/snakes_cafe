from order import Order
import pytest


@pytest.fixture
def order_one():
    return Order()

@pytest.fixture
def order_two():
    return Order()

def test_can_create_Order():
    assert isinstance(order_one, Order)

def test_order_has_id(order_one):
    assert susan_employee.order_id != None

def test_order_id_unique(order_one, order_two):
    assert order_one.order_id != order_two.order_id
