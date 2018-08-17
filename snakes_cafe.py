from textwrap import dedent
from string import Template
from food_bank import BANK
from order import Order
import sys

WIDTH = 96

def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    print('''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    BBQ Wings                       $15.00
    Soup                             $5.00
    Unlimited Bread                  $8.00
    Onion Rings                      $6.00
    Limited Bread                    $4.00
    Cocktail Shrimp                 $11.00
    Spiced Lemon                    $14.00
    Cornbread                        $5.00
    Meat Bun                         $3.00

    Entrees
    -------
    Peking Duck                     $33.00
    Sweet and Sour Pork             $13.00
    Baked Vegetable Platter          $8.00
    Sushi                           $11.00
    Grilled Salmon                  $18.00
    Chicken Parmesean               $14.00
    Avocado Toast                    $2.00
    Turducken                       $32.00
    Monster Steak                   $48.00

    Sides
    -----
    French Fries                     $4.00
    Mashed Potatoes                  $5.00
    Hash Browns                      $3.00
    Baked Potato                     $3.00
    Latkes                           $7.00
    Potatoes Au Gratin               $7.00
    Deluxe Condiments                $2.00
    Spinach                          $2.00
    Vegetable Bun                    $7.00

    Desserts
    --------
    Hot Fudge Sundae                 $6.00
    Pancakes                         $5.00
    Cookies and Milk                 $4.00
    Fluffernutter Sandwich           $3.00
    Ice Cream Mochi                  $8.00
    Bananas Foster                  $10.00
    Banana Split                     $7.00
    Stolen Candy                     $1.00
    Cookie Bun                       $9.00

    Beverages
    ------
    Coffee                           $2.00
    Bubble Tea                       $4.00
    Cola                             $2.00
    Iced Tea                         $2.00
    Green Tea                        $2.00
    Pumpkin Spice Milkshake         $40.00
    Ninja Water                      $6.00
    Better Coffee                    $3.00
    Runny Yogurt                     $5.00

    **************************************
    *** What would you like to order? ****

    Please select an option from the menu.

    You may enter an integer after the
     name of your option to add that
     amount to your order

    To quit at any time, type "quit"
    '''
    )
#    order_one = Order()
#    order_one.add_item('cheeseburger', 2)
#    order_one.food_ordered
# => {'cheeseburger': 2}

def take_order(order_object, customer_order):
    if customer_order.lower() == 'quit':
        exit()
        return
    if customer_order.lower() == 'order':
        crude_display_order()
    else:
        quantity_requested = 1
        split_order = customer_order.split()

        if len(split_order) == 1:
            item_requested = ''.join(split_order)
        elif len(split_order) == 2:
            item_requested = split_order[0]
            quantity_requested = int(split_order[1])

        for item in BANK:
            if item['food'].lower() == item_requested.lower():
                order_object.add_item(item_requested, quantity_requested)
                order_object.price_total += (item['price'] * int(quantity_requested))
                return str(int(quantity_requested)) + ' ' + str(item_requested) + 's were added to the order!'

    return


def crude_price_total():
    print('Your current order total:')
    print('$' + str(ORDER['price_total']))
    print('What else would you like?')


def crude_display_order():
    print('Your current order:')
    print('What else would you like?')


def order_loop(order_object):
    customer_request = input()
    while customer_request != 'quit':
        print(take_order(order_object, customer_request))
        # crude_price_total()
        order_object.display_price_total()
        customer_request = input()


def exit():
    print(dedent('''
    Thank you, come again!
    '''))
    sys.exit()


def run():
    greeting()
    order_object = Order()
    order_loop(order_object)


if __name__ == '__main__':
    run()
