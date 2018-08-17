import uuid

class Order:
    """A class for storing food-order data
    """
    # Every Order should have a uuid
    def __init__(self):
        self.order_id = uuid.uuid4()
        self.items_ordered = {}
        self.price_total = 0.00

    # TODO:
    # The repr of Order instances should look like <Order #ba99d8... | Items: 4 | Total: $754.23>
    def __repr__(self):
        return 'representation under construction'

    # When len() is called on an order instance, the number of items in the order is returned
    def __len__(self):
        return len(self.items_ordered)


    def display_price_total(self):
        print('Your current order total:')
        # TODO:
        print('$' + str(self.price_total))
        print('What else would you like?')

    # add_item takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
    def add_item(self, item_name, quantity):
        if item_name in self.items_ordered:
            if quantity:
                self.items_ordered[item_name] += quantity
            else:
                self.items_ordered[item_name] += 1
        else:
            self.items_ordered[item_name] = 1

    #TODO: Every Order should have a display_order() method that prints the user’s current order to the console
    def display_order(self):
        print('Your current order:')
        print('What else would you like?')

    #TODO: Every menu category should have at least 12 items


    #TODO: Every Order should have a remove_item method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.


    # Every Order should have a print_receipt() method that creates a file containing the text of the user’s full order. The file name should be of the format order-<the uuid>.txt and should have the same output as display_order
    # All of the order input-checking that you used to do will be done by this class
    # The repr of Order instances should look like <Order #ba99d8... | Items: 4 | Total: $754.23>
    # When print() is called on an order instance, the user’s current order is printed as if display_order was called.

    # You may have as many helper methods as you want. However, make sure that any attributes and methods that aren’t intended for public use are prefixed with a single underscore
