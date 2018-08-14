from textwrap import dedent
import sys

WIDTH = 96
BANK = [
    {
        'food_category': 'Appetizers',
        'food': 'BBQ Wings',
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Soup',
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Unlimited Bread',
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Peking Duck',
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Sweet and Sour Pork',
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Baked Vegetable Platter',
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Hot Fudge Sundae',
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Pancakes',
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Cookies and Milk',
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Coffee',
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Bubble Tea',
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Cola',
        'count': 0,
    },
]


def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    print('''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    BBQ Wings
    Soup
    Unlimited Bread

    Entrees
    -------
    Peking Duck
    Sweet and Sour Pork
    Baked Vegetable Platter

    Desserts
    --------
    Hot Fudge Sundae
    Pancakes
    Cookies and Milk

    Beverages
    ------
    Coffee
    Bubble Tea
    Cola

    ***********************************
    ** What would you like to order? **
    ***********************************
    ''')

def take_order(food_order):
    if food_order == 'quit':
        exit()
        return
    return order_update(food_order)


def order_update(food_order):
    for item in BANK:
      if item['food'].lower() == food_order.lower():
        item['count'] += 1
        return str(item['count']) + ' ' + str(item['food']) + 's were added to the order!'
    return 'Please select an option from the menu.'


def exit():
    print(dedent('''
      Thank you, come again!
    '''))
    sys.exit()


def run():
    greeting()
    food_order = input()
    while food_order != 'quit':
      print(take_order(food_order))
      food_order = input()


if __name__ == '__main__':
    run()