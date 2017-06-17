# $368.00 per day
# 0.8333 'days' of vacation per month accrued
# 0.04165 'days' of vacation per work day

total_payout    = 1592.31
accrue_rate     = 0.04165
daily_rate      = 368.00

def get_rough_from_date():
    return total_payout / (daily_rate * accrue_rate)

print get_rough_from_date()
