from cs50 import get_int
import math

# prompt user for credit card
# validate that we have a positive integer between 13 and 16 digits
while True:
    ccNum = get_int('Enter Credit Card Number: ')
    if ccNum >= 0:
        break

# reset value of ccNum
copyCCNum = ccNum
count = 0

# count the number of digits in the integer provided by user
while ccNum > 0:
    ccNum = math.floor(ccNum / 10)
    count += 1

# if user provides a number less than 13 or more than 16, print 'INVALID'
if count < 13 or count > 16:
    print('INVALID')
    quit()

# reset value of ccNum
ccNum = copyCCNum

# access company identifier (2 digits) at the beginning of card number
divNum = 1
if count == 13:
    divNum = 100000000000
elif count == 14:
    divNum = 1000000000000
elif count == 15:
    divNum = 10000000000000
elif count == 16:
    divNum = 100000000000000
identifier = math.floor(ccNum / divNum)

# validate the identifier and assign company to the number if valid
company = ''
if identifier == 34 or identifier == 37:
    company = 'AMEX'
elif identifier >= 40 and identifier <= 49:
    company = 'VISA'
elif identifier >= 51 and identifier <= 55:
    company = 'MASTERCARD'

# if no valid identifier is found, print 'INVALID'
if company == '':
    print('INVALID')

# if card doesn't have required number of digits for the company, print 'INVALID'
if company == 'AMEX' and count != 15:
    print('INVALID')
    quit()
if company == 'VISA' and count < 13:
    print('INVALID')
    quit()
if company == 'VISA' and count > 16:
    print('INVALID')
    quit()
if company == 'MASTERCARD' and count != 16:
    print('INVALID')
    quit()

# validat that we have a real credit card number
# for valid company and number, start with second-to-last digit & multiply every other digit by 2 & then sum those digits
product, splitA, splitB, theSum, secondLastNum = 0, 0, 0, 0, 0
while ccNum > 0:
    ccNum = math.floor(ccNum / 10)
    secondLastNum = math.floor(ccNum % 10)
    product = math.floor(secondLastNum * 2)
    splitA = math.floor(product % 10)
    splitB = math.floor(product / 10)
    theSum = math.floor(theSum + (splitA + splitB))
    ccNum = math.floor(ccNum / 10)
ccNum = copyCCNum

# add sum to remaining digits
lastNum = 0
while ccNum > 0:
    lastNum = math.floor(ccNum % 10)
    ccNum = math.floor(ccNum / 100)
    theSum = math.floor(theSum + lastNum)

# validate checksum
lastNumDigit = theSum % 10
if company == 'AMEX' and lastNumDigit == 0:
    print('AMEX')
    quit()
elif company == 'VISA' and lastNumDigit == 0:
    print('VISA')
    quit()
elif company == 'MASTERCARD' and lastNumDigit == 0:
    print('MASTERCARD')
    quit()
else:
    print('INVALID')
    quit()