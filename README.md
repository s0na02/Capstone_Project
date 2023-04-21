# Bond Valuation Calculator

This is a Python-based bond valuation calculator that can be used to price fixed-rate coupon bonds. The calculator assumes that coupons are paid at regular intervals over the bond life, and that the final coupon is paid on the same date as the principal repayment.

## Inputs

The calculator requires the following inputs to value a bond:


-Face value of the bond

-Coupon rate

-Coupon frequency

-Settlement date (date at which we price the bond)

-Maturity date

-Day count convention: Available conventions are Actual/Actual (ISMA) and 30/360 (Bond Basis).


Additionally, the calculator requires either the price of the bond (clean or dirty) or the yield to maturity (annual) to value the bond.

If you want to price a zero-coupon bond, set the coupon rate to zero.

