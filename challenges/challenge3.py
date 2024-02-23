class SalesItem:
  def __init__(self, branch, totalSales, date):
    self.branch = branch
    self.totalSales = totalSales
    self.date = date

# <summary >
# It has been a busy year at mountain warehouse, having made lots of sales.
# Management would like to know which branch made the most in revenue.
# For this challenge you will be given an array of sales broken down by Branch and Date.
# You will need to sum all branch across multiple days and identify which branch had the highest sales overall
# Assume that there is only one branch with the highest total
# We have provided some starting code but if you know of a better method then go ahead with that
# </summary >
# <param name = "sales" > The array of sales items < /param >
# <returns > The branch with the best performing sales < /returns >


def CalculateBestBranch(sales):

    #print(sales)

    branchSales = {}
    highestSellerBranch = ""
    highestRevenue = 0

    # Implement your code here
    for i in range(len(sales)):
        #print(sales[i].branch , sales[i].totalSales)
        branch, totalSales = sales[i].branch , sales[i].totalSales
        #print (branch, totalSales)
       
        if not branch in branchSales:
            branchSales[branch] = 0 
            
        branchSales[branch] += totalSales

    # order your dictionary by value
    #print(branchSales)
    for branch, totalSale in branchSales.items():
        #print(branch, totalSale)
        if highestRevenue < totalSale:
            highestRevenue = totalSale
            highestSellerBranch = branch
    
    # get key of first item

    return highestSellerBranch
