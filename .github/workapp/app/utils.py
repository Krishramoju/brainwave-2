# Helper functions for calculations or common tasks
def calculate_total_stock_value(products):
    total_value = 0
    for product in products:
        total_value += product.quantity * product.price
    return total_value
