# <summary >
# Receives an amount and returns the total amount including tax.
# </summary >
# <param name = "nonTaxAmount" > The total cost of goods without tax. < /param >
# <param name = "taxRate" > The tax rate to be applied. 50 % = 0.5 < /param >
# <returns > Returns the price including tax. < /returns >
def Add_Tax(nonTaxAmount,  taxRate):
    taxAmount = taxRate * nonTaxAmount
    return nonTaxAmount + taxAmount

# <summary >
# Takes in the current price and returns the price after discount has been deducted.
# If the discount value is not valid then this method should return -1
# </summary >
# <param name = "currentPrice" > The current price of the product. < /param >
# <param name = "discount" > The percentage off of the rrp to be applied. E.g. 10 % = 0.1 < /param >
# <returns > Returns the price after discount. < /returns >


def Discount(currentPrice,  discount):
    if discount >= 1 or discount < 0:
        return -1
    discountAmount = currentPrice * discount
    return currentPrice - discountAmount

# <summary >
# Calculate the total price where two items are part of a "Buy One Get One Half Price" promotion.
# </summary >
# <param name = "item1" > The first item < /param >
# <param name = "item2" > The second item < /param >
# <returns > Returns total value of goods < /returns >


def Buy_One_Get_One_Half_Price(item1,  item2):
    totalAmount = (item1 + (item2 * 0.5)) if item1 > item2 else ((item1 * 0.5) + item2)
    return totalAmount

# <summary >
# Calculates the sum of items within an array.
# </summary >
# <param name = "amounts" >An array of prices </param >
# <returns > Returns total value of goods < /returns >


def Calculate_Total_Cost(amounts):
    return sum(amounts)
