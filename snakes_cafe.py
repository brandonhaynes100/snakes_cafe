from textwrap import dedent
import sys

WIDTH = 96
BANK = [
    {
        'food_category': 'Appetizers',
        'food': 'BBQ Wings',
        'cost': 15,
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Soup',
        'cost': 5,
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Unlimited Bread',
        'cost': 8,
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Onion Rings',
        'cost': 6,
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Limited Bread',
        'cost': 4,
        'count': 0,
    },
    {
        'food_category': 'Appetizers',
        'food': 'Cocktail Shrimp',
        'cost': 11,
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Peking Duck',
        'cost': 33,
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Sweet and Sour Pork',
        'cost': 13,
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Baked Vegetable Platter',
        'cost': 8,
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Sushi',
        'cost': 11,
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Grilled Salmon',
        'cost': 18,
        'count': 0,
    },
    {
        'food_category': 'Entrees',
        'food': 'Chicken Parmesean',
        'cost': 14,
        'count': 0,
    },
    {
        'food_category': 'Sides',
        'food': 'French Fries',
        'cost': 4,
        'count': 0,
    },
    {
        'food_category': 'Sides',
        'food': 'Mashed Potatoes',
        'cost': 5,
        'count': 0,
    },
    {
        'food_category': 'Sides',
        'food': 'Hash Browns',
        'cost': 3,
        'count': 0,
    },
    {
        'food_category': 'Sides',
        'food': 'Baked Potato',
        'cost': 3,
        'count': 0,
    },
    {
        'food_category': 'Sides',
        'food': 'Latkes',
        'cost': 7,
        'count': 0,
    },
    {
        'food_category': 'Sides',
        'food': 'Potatoes Au Gratin',
        'cost': 7,
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Hot Fudge Sundae',
        'cost': 6,
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Pancakes',
        'cost': 5,
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Cookies and Milk',
        'cost': 4,
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Fluffernutter Sandwich',
        'cost': 3,
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Ice Cream Moci',
        'cost': 8,
        'count': 0,
    },
    {
        'food_category': 'Desserts',
        'food': 'Bananas Foster',
        'cost': 10,
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Coffee',
        'cost': 2,
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Bubble Tea',
        'cost': 4,
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Cola',
        'cost': 2,
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Iced Tea',
        'cost': 2,
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Green Tea'
        'cost': 2,
        'count': 0,
    },
    {
        'food_category': 'Beverages',
        'food': 'Pumpkin Spice Milkshake',
        'cost': 40,
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
    BBQ Wings                       $15.00
    Soup                             $5.00
    Unlimited Bread                  $8.00
    Onion Rings                      $6.00
    Limited Bread                    $4.00
    Cocktail Shrimp                 $11.00

    Entrees
    -------
    Peking Duck                     $33.00
    Sweet and Sour Pork             $13.00
    Baked Vegetable Platter          $8.00
    Sushi                           $11.00
    Grilled Salmon                  $18.00
    Chicken Parmesean               $14.00

    Sides
    -----
    French Fries                     $4.00
    Mashed Potatoes                  $5.00
    Hash Browns                      $3.00
    Baked Potato                     $3.00
    Latkes                           $7.00
    Potatoes Au Gratin               $7.00

    Desserts
    --------
    Hot Fudge Sundae                 $6.00
    Pancakes                         $5.00
    Cookies and Milk                 $4.00
    Fluffernutter Sandwich           $3.00
    Ice Cream Mochi                  $8.00
    Bananas Foster                  $10.00

    Beverages
    ------
    Coffee                           $2.00
    Bubble Tea                       $4.00
    Cola                             $2.00
    Iced Tea                         $2.00
    Green Tea                        $2.00
    Pumpkin Spice Milkshake         $40.00

    ***********************************
    ** What would you like to order? **
    ***********************************
    ''')

def take_order(food_order):
    if food_order == 'quit':
        exit()
        return
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
