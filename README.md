# Bond Valuation Calculator

This is a Python-based bond valuation calculator that can be used to price fixed-rate coupon bonds. The calculator assumes that coupons are paid at regular intervals over the bond life, and that the final coupon is paid on the same date as the principal repayment.

## Inputs

The calculator requires the following inputs to value a bond:


***-Principal or face value of the bond***

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
## Bond Calculator
Computes bond YTM, price, duration, or convexity.
Run from a Command Line Interface (CLI).

## Installation
Installation is simply downloading the code from GitHub. Enter the following at a terminal prompt to install in your home directory:
```bash
$ cd
$ git clone https://github.com/shreysrins/bond-calculator.git
```

## Dependencies
This code was developed and tested in Python 3.7. You can check your version of Python with the following terminal command:
```bash
$ python3 --version
```

Install all dependencies by opening a terminal and running:
```bash
$ pip3 install -r requirements.txt
```
 - pyfiglet >= 0.8.post1 (`pip3 install pyfiglet`)
 - NumPy ~= v1.19.4 (`pip3 install numpy`)
 - SciPy ~= v1.6.2 (`pip3 install scipy`)

## Usage
Open a terminal and navigate to the directory in which this repository is stored. If you installed in your home directory, this is done with:
```bash
$ cd ~/bond-calculator/
```
The command to run the calculator is:
```bash
$ python3 bond_calc.py
```
All instructions and prompts are given in the terminal itself.

## Updating
To check for and install updates: open a terminal, navigate to the directory in which this repository is stored, and run the `git pull` command. If you installed in your home directory, this is done with:
```bash
$ cd ~/bond-calculator/
$ git status
$ git pull
```
