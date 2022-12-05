# NPV Calculator
# Calculates the Net Present Value of all cash flows over the life of a project

print("###########################################################################")
print("NPV (Net Present Value) Calculator")
print("The NPV calculator will calculate the total net present value of all cash flows received over the life of a project.")
print("###########################################################################")


initInvestment = 0 #initial investment
numcashFlow = 0 #number of cashflows
discountRate = 0 #interest rate
npvTotal = 0 # NPV total
cashFlow = {} #Cashflow data store


print("Please enter the initial investment amount?")
initInvestment = int(input())

print("Please enter the amount of Cash Flows?")
numcashFlow = int(input())

print("Please enter the dicount rate? (ie 0.03 for 3%)")
discountRate = float(input())


#Enter in the cashFlows to the dictionary data store
cf = 1
for x in range(numcashFlow):
    print("Please enter the cash flow amount at year {}?".format(cf))
    cfamt = int(input())
    cashFlow.update({cf: cfamt})
    cf = cf + 1


#Loop through and complete the npv calculation on each cash flow
ncf = 1
for x in cashFlow:
    npval = cashFlow[ncf]
    irate = 1 + discountRate
    ncalc = irate**ncf
    npval = npval/ncalc
    npval = round(npval, 2)
    cashFlow[ncf] = npval
    ncf = ncf + 1


#Sum up the net cash flows
for x in cashFlow:
    npval = cashFlow[x]
    npvTotal += npval

#print(npvTotal) #- Check


#Calculate the total NPV minus the initial investment
npvCalc = npvTotal - initInvestment
npvCalc = round(npvCalc, 2)
print("The total Net Present Value is:")
print(npvCalc)



