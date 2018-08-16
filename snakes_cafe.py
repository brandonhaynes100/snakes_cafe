from textwrap import dedent
from string import Template
from food_bank import BANK
from order import ORDER
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

def take_order(customer_order):
    if customer_order.lower() == 'quit':
        exit()
        return
    if customer_order.lower() == 'order':
        order_summary()
    else:
        quantity = 1
        split_order = str(customer_order).split()
        # if len(split_order) == 1:

        for item in BANK:
            if item['food'].lower() == customer_order.lower():
                item['quantity'] += quantity
                return str(item['quantity']) + ' ' + str(item['food']) + 's were added to the order!'
    return

def order_price_total():

    print('Your current order total:')
    print('$' + str(ORDER['price_total']))
    print('What else would you like?')


def order_summary():
    print('Your current order:')
    print('What else would you like?')


def order_loop():
    customer_order = input()
    while customer_order != 'quit':
        print(take_order(customer_order))
        order_price_total()
        customer_order = input()


def exit():
    print(dedent('''
      Thank you, come again!
    '''))
    sys.exit()


def run():
    greeting()
    order_loop()

if __name__ == '__main__':
    run()
