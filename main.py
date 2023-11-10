print("Welcome to the tip calculator.")
userTotalBill = input("what was the total bill? $")
print(userTotalBill)
userPercentageTip = input("What percentage tip would you like to give? ")
print(userPercentageTip)
userNumberofPeople = input("How many people to split the bill? ")
print(userNumberofPeople)

intTotalBill = float(userTotalBill)  #convert string input to int
intPercentageTip = int(userPercentageTip)  #convert string input to int
percentageofTip = float(intPercentageTip /
                        100)  #convert string input to float like .12 1.20
intNumberofPeople = int(userNumberofPeople)  # convert string input to int

totalBillPercentageTip = intTotalBill * percentageofTip  # get the amount of tip base on percentage and to be added to total bill later
totalBillincludingTip = intTotalBill + totalBillPercentageTip  # the total bill and the amount of tip(base on the percentage)

print(f"Total bill is {totalBillincludingTip}")

eachPersonPay = round(totalBillincludingTip / intNumberofPeople,
                      2)  #round to 2 decimal places
print(f"Each person should pay: ${eachPersonPay}")

final_amount_of_bill = "{:.3f}".format(
    totalBillincludingTip)  #rount the float to 3 decimal places
print(final_amount_of_bill)
