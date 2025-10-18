# Supermarket Cashier Project
# Author: ThriveSphere Global TV
# License: MIT

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit: ").upper()
        if details == "A":
            product = input("Enter product: ").capitalize()
            quantity = int(input("Enter quantity: "))
            buyingData.update({product: quantity})
        elif details == "Q":
            enterDetails = False
        else:
            print("Please select a correct option (A or Q).")
    return buyingData


def getPrice(product, quantity):
    priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }
    if product not in priceData:
        print(f"{product} is not available in the price list.")
        return 0

    subtotal = priceData[product] * quantity
    print(f"{product}: ${priceData[product]} x {quantity} = ${subtotal}")
    return subtotal


def getDiscount(billAmount, membership):
    discount = 0
    membership = membership.capitalize()
    
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount *= 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount *= 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount *= 0.95
            discount = 5
        
        if discount > 0:
            print(f"{discount}% off for {membership} membership on total amount: ${billAmount:.2f}")
    else:
        print("No discount on amount less than $25.")
    return billAmount


def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    
    billAmount = getDiscount(billAmount, membership)
    print(f"The final discounted amount is: ${billAmount:.2f}")


if __name__ == "__main__":
    buyingData = enterProducts()
    membership = input("Enter customer membership (Gold/Silver/Bronze): ")
    makeBill(buyingData, membership)
