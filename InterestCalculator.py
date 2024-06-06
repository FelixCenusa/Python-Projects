import time
start = time.time()
# print all things that the user should input first
print("1. Initial balance: ")
print("2. Duration of investment in years: ")
print("3. Would you like to add deposit yearly or monthly: Y/M")
print("4. Annual / Monthly deposit amount: ")
print("5. Annual interest rate: ")
print("6. Annual inflation rate: ")
print("")
# this time lets ask the user to input the values
balanceInitial = float(input())
# for how long would the user like to invest in years
Duration = int(input())
# would the user like to add deposit yearly or monthly
YearlyOrMonthly = input()
DepositoPeriodico = float(input())
# what is the annual interest rate
IntresAnual = float(input())
# what is the annual inflation rate
Inflatie = float(input())
# lets calculate the total amount of money after the duration
Total = balanceInitial
# lets calculate the interest rate with inflation
InteresAnualConInflatie = IntresAnual - Inflatie + 1
# lets print the initial balance
print(chr(27) + "[2J" + chr(27) + "[;H")
print("Initial balance: ", balanceInitial)
# lets make the InteresAnualConInflatie into a variable that has the monthly interest rate
MonthlyInterestRate = (InteresAnualConInflatie/100 + 1) ** (1.0 / 12)
print("Testing monthly interest rate: ", MonthlyInterestRate**12, (InteresAnualConInflatie/100 + 1))
# lets calculate the total amount of money after the duration if the user chose to deposit monthly and calculate the interest 12 times per year
if YearlyOrMonthly == "M":
    for i in range(Duration * 12):
        Total += DepositoPeriodico 
        Total *= MonthlyInterestRate
        print("Money increasing monthly: ", round(Total,0))

# lets calculate the total amount of money after the duration if the user chose to deposit yearly and calculate the interest 1 time per year
else:
    for i in range(Duration):
        Total += DepositoPeriodico 
        Total *= InteresAnualConInflatie
        print("Money increasing yearly: ", round(Total,0))

# lets print the total amount of profit after the duration
if YearlyOrMonthly == "M":
    print("After ", Duration, " years you will have this much money: ", round(Total,0))
    print("You added this much money every Month / Year: ", DepositoPeriodico)
    if YearlyOrMonthly == "M":
        print("In total you added this much money: ", DepositoPeriodico * Duration * 12)
    else:
        print("In total you added this much money: ", DepositoPeriodico * Duration)
    amountOfProfitFromInterestOnly = (Total - balanceInitial) - (DepositoPeriodico * Duration * 12)
    print("That means you will have this much extra profit: ", round(amountOfProfitFromInterestOnly,2))
    print("That means you will have this much extra profit in percentage: ", round((amountOfProfitFromInterestOnly / balanceInitial * 100),2), "%")
stop = time.time()
print("Time to run program: ", round((stop - start),2)," seconds")