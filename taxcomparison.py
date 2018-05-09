#!/usr/bin/python

def calcProfitAfterTax(investedAmount,returnPercent,income_tax_percent):

	print "Investment: $" + str(investedAmount)
	#print "Return Before Taxes: " + ""+str(100*returnPercent)+"% ($" + str(returnPercent*investedAmount) +")"
	print("Return Before Taxes: %.2f%% ($%.2f)" % (100*returnPercent,returnPercent*investedAmount))


	returnAmount = investedAmount * returnPercent
	returnValueCapGains= returnAmount - (.15 * returnAmount)
	returnValueCapGainsPercent = returnValueCapGains/investedAmount
	print("Return after Capital Gains Tax(15%%) : %.2f%% ($%.2f)" % (returnValueCapGainsPercent*100,returnValueCapGains))

	# 2014 income tax is 89k-16k, pays 18k plus 35% of anyting over
	#http://www.forbes.com/sites/kellyphillipserb/2013/10/31/irs-announces-2014-tax-brackets-standard-deduction-amounts-and-more/
	returnValueIncomeTax= returnAmount - (income_tax_percent * returnAmount)
	returnValueIncomeTaxPercent = returnValueIncomeTax/investedAmount
	print("Return after Income Tax(%.2f%% ) : %.2f%% ($%.2f)" % (income_tax_percent * 100,returnValueIncomeTaxPercent*100,returnValueIncomeTax))

	returnNeeded = returnValueCapGains/(1-income_tax_percent)
	interestNeeded = returnNeeded/investedAmount
	print("Return percent for getting equivalent cap gain : %.2f%%" % (interestNeeded*100))


banner = "\nThis utility compares what the returns would be between \ninvestments that are taxed under Capital \
Gains vs \nIncome Tax. It shows the return percentage you need \nto get the same after tax return as a Capital \
Gains \ninvestment.\n"

print banner

investedAmount = raw_input("Enter investment amount: ")
returnPercent = raw_input("Enter return percent: ")
income_tax = raw_input("Enter income tax percent:")

calcProfitAfterTax(float(investedAmount),float(returnPercent)/100,float(income_tax)/100)
