#!/usr/bin/python

def calcProfitAfterTax(investedAmount,returnPercent):

	

	print "Investment: $" + str(investedAmount)
	#print "Return Before Taxes: " + ""+str(100*returnPercent)+"% ($" + str(returnPercent*investedAmount) +")"
	print("Return Before Taxes: %.2f%% ($%.2f)" % (100*returnPercent,returnPercent*investedAmount))

	
	returnAmount = investedAmount * returnPercent
	returnValueCapGains= returnAmount - (.15 * returnAmount)
	returnValueCapGainsPercent = returnValueCapGains/investedAmount
	print("Return after Capital Gains Tax(15%%) : %.2f%% ($%.2f)" % (returnValueCapGainsPercent*100,returnValueCapGains))
	
	# 2014 income tax is 89k-16k, pays 18k plus 28% of anyting over
	#http://www.forbes.com/sites/kellyphillipserb/2013/10/31/irs-announces-2014-tax-brackets-standard-deduction-amounts-and-more/
	returnValueIncomeTax= returnAmount - (.28 * returnAmount)
	returnValueIncomeTaxPercent = returnValueIncomeTax/investedAmount
	print("Return after Income Tax(28%%) : %.2f%% ($%.2f)" % (returnValueIncomeTaxPercent*100,returnValueIncomeTax))

	returnNeeded = returnValueCapGains/(.72)	
	interestNeeded = returnNeeded/investedAmount
	print("Return percent for getting equivalent cap gain : %.2f%%" % (interestNeeded*100))


banner = "\nThis utility compares what the returns would be between \ninvestments that are taxed under Capital \
Gains vs \nIncome Tax. It shows the return percentage you need \nto get the same after tax return as a Capital \
Gains \ninvestment.\n"

print banner

investedAmount = raw_input("Enter investment amount: ")
returnPercent = raw_input("Enter return percent: ")

calcProfitAfterTax(float(investedAmount),float(returnPercent)/100)