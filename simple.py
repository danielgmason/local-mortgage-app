''' mortgage_loan_calc1.py
calculate the monthly payment on a mortgage loan
tested with Python27 and Python33
'''
import math
def calc_mortgage_bank(bank_principal, bank_interest, bank_years):
    '''
    given mortgage loan principal, interest(%) and years to pay
    calculate and return monthly payment amount
    '''
    # monthly rate from annual percentage rate
    interest_rate_calc_bank = bank_interest/(100 * 12)
    # total number of payments
    payment_num_bank_calc = bank_years * 12
    # calculate monthly payment
    monthly_bank_payment = bank_principal * \
    (interest_rate_calc_bank / (1-math.pow((1+interest_rate_calc_bank), (-payment_num_bank_calc))))
    return monthly_bank_payment


def calc_mortgage_family(family_principal, family_interest, family_years):
    '''
    this calculates the second part of the mortgage, that's provided outside
    of the bank loan
    '''
    # monthly rate form annual percentage rate
    interest_rate_family = family_interest/(100*12)
    # total number of payments
    payment_num_family = family_years * 12
    # calcullate monthly payments
    payment_family = family_principal * \
        (interest_rate_family/(1-math.pow((1+interest_rate_family), (-payment_num_family))))
    return payment_family


## EDITABLE INFORMATION
# down payment
purchase_price = 399000
down_payment = 100000
monthly_hoas = 610
annual_taxes = 4915
bank_mortgage_total = 100000
monthly_insurance = 80

## BANK MORTAGE INFORMATION
# bank mortgage amount
bank_principal = bank_mortgage_total
#bank annual interest
bank_interest = 3.4
# years to pay off mortgage
bank_years = 30

## FAMILY MORTAGE INFORMATION
# family mortgage amount
family_principal = purchase_price - down_payment - bank_principal
#family annual interest
family_interest = 2.0
# years to pay off mortgage
family_years = 30


# calculate monthly payment amount frp, baml
monthly_payment_bank = calc_mortgage_bank(bank_principal, bank_interest, bank_years)

# calculate monthly payment amount
monthly_payment_family = calc_mortgage_family(family_principal, family_interest, family_years)

# combine the two mortages


total_monthly_mortgage_amount = int(monthly_payment_bank) + int(monthly_payment_family)

total_monthly_cost = total_monthly_mortgage_amount + monthly_hoas + (annual_taxes/12) + monthly_insurance
# calculate total amount paid
total_mortgage_amount = int(monthly_payment_bank * bank_years * 12) + int(monthly_payment_family * family_years * 12)

total_30_year_costs = total_mortgage_amount + (annual_taxes*bank_years) + (monthly_hoas * 12 * bank_years) + (monthly_insurance * 12 * bank_years)
# show result ...
# {:,} uses the comma as a thousands separator
print('-'*40)
print 'START:::'
print('-'*40)
print 'BANK PORTION:'
sf = '''\
For a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''
print(sf.format(bank_years, bank_principal, bank_interest, monthly_payment_bank))
print('-'*40)
print '2nd MORTGAGE PORTION:'
sf = '''\
For a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''
print(sf.format(family_years, family_principal, family_interest, monthly_payment_family))
print('-'*40)
print 'TOTAL:'
sf = '''\
The Total Monthly Mortgage Payment is ${:,.2f}'''
print (sf.format(total_monthly_mortgage_amount))
print('-'*40)
print 'ADDITIONAL MONTHLY COSTS:'
sf = '''\
Monthly HOAs : ${:,.2f}'''
print (sf.format(monthly_hoas))
sf = '''\
Monthly Taxes : ${:,.2f}'''
print (sf.format(annual_taxes/12))
sf = '''\
Monthly Insurance : ${:,.2f}'''
print (sf.format(monthly_insurance))
print('-'*40)
print 'TOTAL ALL-IN MONTHLY COSTS:'
sf = '''\
Total costs are : ${:,.2f}'''
print (sf.format(total_monthly_cost))
print('-'*40)
print 'LIFETIME OF MORTAGE (30 Years):'
print("Total mortgage paid will be ${:,.2f}".format(total_mortgage_amount))
print("Total all-in costs (at current levels) will be : ${:,.2f}".format(total_30_year_costs))
print('-'*40)

''' result ...
For a 30 year mortgage loan of $100,000
at an annual interest rate of 7.50%
you pay $699.21 monthly
----------------------------------------
Total amount paid will be $251,717.22
'''