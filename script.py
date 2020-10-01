# Different types of pizzas
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print( "We sell "+ str(num_pizzas) + " different kinds of pizza!.")
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza = pizzas[1]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[0:3]
print(three_cheapest)
num_two_doller_slices = prices.count(2)
print("Cheapest pizza is",cheapest_pizza)
print("Priciest pizza is",priciest_pizza)



