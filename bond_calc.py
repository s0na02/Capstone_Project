import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scipy import optimize


def test(values):
    principal_value = float(values[0])
    coupon_rate = float(values[1])
    coupon_frequency = float(values[2])
    settlement_date = values[3]
    maturity_date = values[4]
    yield_to_maturity = float(values[5])
    convention = values[6]
    dirty_price = None
    clean_price = None

    coupon_amount = principal_value * (coupon_rate / coupon_frequency)
    settlement_date = datetime.strptime(settlement_date, '%d/%m/%Y').date()
    maturity_date = datetime.strptime(maturity_date, '%d/%m/%Y').date()
    coupon_months = int(12 / coupon_frequency)

    # Compute cash flow dates
    cflow_date = maturity_date
    cflow_dates = [maturity_date]
    while cflow_date + relativedelta(months=-coupon_months) > settlement_date:
        cflow_date += relativedelta(months=-coupon_months)
        cflow_dates.append(cflow_date)
    cash_flow_dates = cflow_dates[::-1]

    # Compute accrued interest
    next_coupon_date = cash_flow_dates[0]
    previous_coupon_date = next_coupon_date + relativedelta(months=-coupon_months)
    if convention == 'ACT/ACT':
        accrued_days = (settlement_date - previous_coupon_date).days
        curr_coupon_days = (next_coupon_date - previous_coupon_date).days
        accrual_period = accrued_days / curr_coupon_days
        accrued_interest = principal_value * (
                    coupon_rate / coupon_frequency) * accrual_period
    elif convention == '30/360':
        d1 = min(30, previous_coupon_date.day)
        if d1 == 30:
            d2 = min(d1, settlement_date.day)
        else:
            d2 = settlement_date.day
        accrued_days = 360 * (settlement_date.year - previous_coupon_date.year) + 30 * (
                    settlement_date.month - previous_coupon_date.month) + d2 - d1
        curr_coupon_days = 360 / coupon_frequency
        accrual_period = accrued_days / curr_coupon_days
        accrued_interest = principal_value * (
                    coupon_rate / coupon_frequency) * accrual_period
    elif convention == 'ACT/360':
            accrued_days = (settlement_date - previous_coupon_date).days    
            curr_coupon_days = 360 / coupon_frequency
            accrual_period = accrued_days / curr_coupon_days
            accrued_interest = principal_value * (coupon_rate / coupon_frequency) * accrual_period
    elif convention == 'ACT/365':
            accrued_days = (settlement_date - previous_coupon_date).days
            curr_coupon_days = (next_coupon_date - previous_coupon_date).days
            accrual_period = accrued_days / 365
            accrued_interest = principal_value * (coupon_rate / coupon_frequency) * accrual_period
    

    # Compute cash flow amounts and time to cash flows and maturity
    first_tau = (curr_coupon_days - accrued_days) / curr_coupon_days
    cash_flow_amounts = []
    taus = []
    for i in range(len(cash_flow_dates)):
        cash_flow_amounts.append(coupon_amount)
        taus.append((first_tau + i) / coupon_frequency)
    cash_flow_amounts[-1] += principal_value
    cash_flows = np.array(cash_flow_amounts)
    taus = np.array(taus)
    time_to_maturity = taus[-1]

    # Compute clean and dirty prices
    if dirty_price:
        dirty_price = dirty_price
        clean_price = dirty_price - accrued_interest
    elif clean_price:
        clean_price = clean_price
        dirty_price = clean_price + accrued_interest
    elif yield_to_maturity:
        yield_to_maturity = yield_to_maturity
        ytm_adjusted = coupon_frequency * np.log(1 + yield_to_maturity / coupon_frequency)
        discount_factors = np.exp(-ytm_adjusted * taus)
        dirty_price = np.sum(cash_flows * discount_factors)
        clean_price = dirty_price - accrued_interest

    # Compute current yield
    current_yield = (coupon_rate * principal_value) / dirty_price

    # Compute yield to maturity
    if yield_to_maturity:
        yield_to_maturity = yield_to_maturity
        ytm_adjusted = coupon_frequency * np.log(1 + yield_to_maturity / coupon_frequency)
    else:
        def get_bond_price(yield_to_maturity, cash_flows, taus):
            return np.sum(cash_flows * np.exp(-yield_to_maturity * taus))

        get_ytm = lambda ytm: get_bond_price(ytm, cash_flows, taus) - dirty_price

        ytm_adjusted = optimize.newton(get_ytm, 0.04)
        yield_to_maturity = (np.exp(ytm_adjusted / coupon_frequency) - 1) * coupon_frequency
        discount_factors = np.exp(-ytm_adjusted * taus)

    # Compute duration
    first_derivative = np.sum(-taus * cash_flows * discount_factors)
    duration_macaulay = -1 / dirty_price * first_derivative
    duration_modified = duration_macaulay / (1 + yield_to_maturity / coupon_frequency)

    # Compute convexity
    second_derivative = np.sum(taus ** 2 * cash_flows * discount_factors)
    convexity = 1 / dirty_price * second_derivative

    # Generate summary table
    index = ['Dirty price', 'Clean price', 'Accrued interest', 'Face value', 'Coupon rate', 'Coupon frequency',
             'Yield to maturity',
             'Time to maturity', 'Macaulay duration', 'Modified duration', 'Convexity', 'Settlement date',
             'Maturity date', 'Convention']
    data = list(np.round(
        [dirty_price, clean_price, accrued_interest, principal_value, coupon_rate,
         coupon_frequency,
         yield_to_maturity, time_to_maturity, duration_macaulay, duration_modified,
         convexity], 2))
    data += [settlement_date, maturity_date, convention]
    return data
