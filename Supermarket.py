
shopping_list = ["apple", "pear", "banana"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
        print(key)
        if stock[key] > 0:
            total += prices[key]
            stock[key] -= 1
            print("price: %s" % prices[key])
        else:
            print("no item")
            print("price: 0")
        print
    return total


print(compute_bill(shopping_list))
