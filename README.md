# Bond Valuation Calculator

This is a Python-based bond valuation calculator that can be used to price fixed-rate coupon bonds. The calculator assumes that coupons are paid at regular intervals over the bond life, and that the final coupon is paid on the same date as the principal repayment.

## Inputs

The calculator requires the following inputs to value a bond:


***-Face value of the bond***

***-Coupon rate***

***-Coupon frequency***

***-Settlement date (date at which we price the bond)***

***-Maturity date***

***-Day count convention:*** Available conventions are Actual/Actual (ISMA) and 30/360 (Bond Basis).


Additionally, the calculator requires either the ***price of the bond (clean or dirty)*** or the ***yield to maturity (annual)*** to value the bond.

If you want to price a zero-coupon bond, set the coupon rate to zero.

## Usage

The bond valuation calculator is implemented in the form of a Python class. To use the calculator, simply instantiate the class and provide the required inputs.

Here is an example of how to use the calculator:

```ruby
# Parameters
principal_value = 1125
coupon_rate = 0.065
coupon_frequency = 2
settlement_date = '12/01/2019'
maturity_date = '20/04/2030'
yield_to_maturity = 0.045
convention='30/360'

# Instantiate bond
bond = bond_pricer(principal_value=principal_value, coupon_rate=coupon_rate, coupon_frequency=coupon_frequency, 
                settlement_date=settlement_date, maturity_date=maturity_date, 
                yield_to_maturity=yield_to_maturity, convention=convention)

# Print bond metrics
bond.print_summary()
```
