"""
Author: Ben Hilarides
Date: 8.31.25
File Name: hilarides_lemonadeStand.py
Description: This file demonstrates the use of both file header comments and normal
level comments

"""

# Defining the calculate_cost function
def calculate_cost(lemons_cost, sugar_cost):
    """
    This function calculates the total cost of ingredients for the lemonade stand.

    Parameters:
    lemons_cost (float): Cost of lemons
    sugar_cost (float): Cost of sugar

    Returns:
    float: Total cost of ingredients
    """
    total_cost = lemons_cost + sugar_cost # Calculating the total cost
    return total_cost # Returning the total cost

# Defining the calculate_profit function
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    """
    This function calculates the profit from selling lemonade.

    Parameters:
    lemons_cost (float): Cost of lemons
    sugar_cost (float): Cost of sugar
    selling_price (float): Price at which lemonade is sold

    Returns:
    float: Profit from selling lemonade
    """
    total_cost = calculate_cost(lemons_cost, sugar_cost) # Getting the total cost
    profit = selling_price - total_cost # Calculating the profit
    return profit # Returning the profit

# Creating test variables for costs and selling price
lemons_cost = 2.50 # Cost of lemons
sugar_cost = 2.00 # Cost of sugar
selling_price = 6.00 # Selling price of lemonade

# Testing calculate_cost function
total_cost = calculate_cost(lemons_cost, sugar_cost) # Calculating total cost
cost_results = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(total_cost) # Formatting the cost results
print(cost_results) # Printing the cost results

# Testing calculate_profit function
profit = calculate_profit(lemons_cost, sugar_cost, selling_price) # Calculating profit
profit_results = "Selling at " + str(selling_price), "profit is " + str(profit) # Formatting the profit results
print(profit_results) # Printing the profit results