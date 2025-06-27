# basic
def compoundInterestBasic(startingAmount, interestRate, yearlyDeposits, yearsInvested):
    balancePerYear = [startingAmount]
    for years in range(yearsInvested):
        balancePerYear.append((balancePerYear[-1] + yearlyDeposits) + ((balancePerYear[-1] + yearlyDeposits) * (interestRate / 100)))
    return balancePerYear

# monthly deposits at the beginning of each month, compounding yearly
def compoundInterestMonthly(startingAmount, interestRate, monthlyDeposits, yearsInvested):
    balancePerMonth = [startingAmount]
    depositsPerMonth = [startingAmount]
    interestPerMonth = [0]
    totalDepositsPerMonth = [startingAmount]
    totalInterestPerMonth = [0]

    months = yearsInvested * 12

    for month in range(1, months + 1):
        # add deposits first, as they get put in at the start of the year
        depositsPerMonth.append(monthlyDeposits)
        totalDepositsPerMonth.append(totalDepositsPerMonth[-1] + monthlyDeposits)

        # just keeping a running total here
        balancePerMonth.append(balancePerMonth[-1] + monthlyDeposits)

        # calculating interest on the principle
        interestPerMonth.append(balancePerMonth[-1] * (interestRate / 100 / 12))
        totalInterestPerMonth.append(totalInterestPerMonth[-1] + interestPerMonth[-1])

        # should we compound here? yes if it is at the end of the year
        youShouldCompound = month % 12 == 0

        # compound, adding the interest from the past 12 months to the principle
        if youShouldCompound:
            balancePerMonth[-1] = balancePerMonth[-1] + sum(interestPerMonth[-12:])


    return balancePerMonth


