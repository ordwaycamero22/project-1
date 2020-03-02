#Cameron Ordway, block 5, project 1
#in this project we will create a program that calculates the price of a car payment including insurance 
#Getting inputs from user to determing the base payment they will be making
carPrice = float(input("How much is the car you are getting? "))
loanLength = int(input("How many months do you want to be paying? "))
#Calculating monthly payment before interest
monthlyPayment = carPrice/loanLength
print("Your monthly payment before interest is ",monthlyPayment,)
#Determining an interest rate based of credit score and the condition of the car
creditScore = int(input("What is your credit score? 300-850. "))
carCondition = input("Is your car new or used? ")
if (creditScore>=781)and (carCondition == "new"or carCondition == "New"):
  interestRate = 4
  print("Your interest rate is",interestRate,)
elif (creditScore>=661)and (carCondition == "new"or carCondition == "New"):
  interestRate = 5.5
  print("Your interest rate is",interestRate,)
elif (creditScore>= 601)and (carCondition == "new" or carCondition == "New"):
  interestRate = 8
  print("Your interest rate is",interestRate,)
elif (creditScore>=501)and(carCondition == "new"or carCondition == "New"):
  interestRate = 13.8
  print("Your interest rate is",interestRate,)
elif (creditScore>=300)and (carCondition == "new"or carCondition == "New"):
  interestRate = 16.3
  print("Your interest rate is",interestRate,)
elif (creditScore>=781)and (carCondition == "used"or carCondition == "Used"):
  interestRate = 3.5
  print("Your interest rate is",interestRate,)
elif (creditScore>=661)and (carCondition == "used"or carCondition == "Used"):
  interestRate = 4.5
  print("Your interest rate is",interestRate,)
elif (creditScore>= 601)and (carCondition == "used" or carCondition == "Used"):
  interestRate = 7.5
  print("Your interest rate is",interestRate,)
elif (creditScore>=501)and(carCondition == "used"or carCondition == "Used"):
  interestRate = 12
  print("Your interest rate is",interestRate,)
elif (creditScore>=300)and (carCondition == "used"or carCondition == "Used"):
  interestRate = 15
  print("Your interest rate is",interestRate,)
elif(creditScore>850 or creditScore<300):
  print("That is not a valid credit score.")
else:
  print("That is not valid.")
if(creditScore>850 or creditScore<300):
  print("That is not a valid credit score.")
#Calculating and printing the monthly cost with interest
monthlyInterest= ((((interestRate%100)*monthlyPayment)+monthlyPayment)/60)+monthlyPayment
print("Your cost with interest is now ",monthlyInterest)
#Finding what their insurance cost will be with a function
def InsuranceCost(x):
  if (userInsurance == 1):
    monthlyInsurance = 68
    return monthlyInsurance
  elif (userInsurance == 2):
    monthlyInsurance = 112
    return monthlyInsurance
  elif(userInsurance == 3):
    monthlyInsurance= 126
    return monthlyInsurance
  elif(userInsurance==4):
    monthlyInsurance = 130
    return monthlyInsurance
  elif(userInsurance == 5):
    monthlyInsurance= 157
    return monthlyInsurance
  else:
    print("That is not a valid insurance.")
#Getting the input for insurance
userInsurance = int(input("What insurance do you have? 1 for Geico, 2 for State Farm, 3 for Farmers, 4 for Progressive, or 5 for Allstate?"))
#Printing the return value from the function
print("The monthly insurance price is %f."%(InsuranceCost(userInsurance)))
InsuranceCost(userInsurance)
#Calculating total monthly cost, then printing the values building up as they go through their payment. I had to use numpy to allow me to keep the numbers as floats in my loop, because for loops usually want integers
totalMonthly= InsuranceCost(userInsurance)+monthlyInterest
import numpy as np
for a in np.arange(0,(totalMonthly * loanLength)+1, totalMonthly):
   print("For this month, the total amount paid including insurance is %.3f."%a)
print("Your total monthly payment will be",totalMonthly,",including insurance.")
