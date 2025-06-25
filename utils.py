def compoundInterest(startingAmount, interestRate, yearlyDeposits, yearsInvested):
    pricePerYear = [startingAmount]
    for years in range(yearsInvested):
        pricePerYear.append((pricePerYear[-1] + yearlyDeposits) + ((pricePerYear[-1] + yearlyDeposits) * (interestRate / 100)))
    return pricePerYear
