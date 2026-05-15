#15-05-2026 | 15-05-2026

'''
    Problem:
            Given a string describing a coffee order, identify all matching menu items and return a formatted order summary.

    Args:
            order (str): A string containing a coffee order.
    
    Return:
            str: A formatted string containing matched menu items and total price.
'''

def format_coffee_order(order):
  
    menu_prices = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75
    }

    items = [item for item in menu_prices if item in order.lower()]
    total_price = sum(menu_prices[item] for item in items)

    return f"{' + '.join(items)}: ${total:.2f}"
