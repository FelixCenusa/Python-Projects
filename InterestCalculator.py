# This program is a simple interest calculator that calculates the total amount of money after a certain amount of years. 
# The user can choose to deposit money monthly or yearly. The user can also choose the interest rate and the inflation rate. 
# The program will calculate the total amount of money after the duration and the total amount of profit. 
# The program will also calculate the total amount of profit in percentage. 
# The program will also calculate the time it took to run the program. 
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
balanceInitial = float(input())
Duration = int(input())
YearlyOrMonthly = input()
DepositoPeriodico = float(input())
IntresAnual = float(input())
Inflatie = float(input())
Total = balanceInitial
InteresAnualConInflatie = IntresAnual - Inflatie
print(chr(27) + "[2J" + chr(27) + "[;H")
print("Initial balance: ", balanceInitial)
MonthlyInterestRate = (InteresAnualConInflatie/100 + 1) ** (1.0 / 12)
print("Testing monthly interest rate: ", MonthlyInterestRate**12, (InteresAnualConInflatie/100 + 1))
if YearlyOrMonthly == "M":
    for i in range(Duration * 12):
        Total *= MonthlyInterestRate
        Total += DepositoPeriodico 
        print("Money increasing monthly: ", round(Total,0))

else:
    for i in range(Duration):
        Total *= 1 + (InteresAnualConInflatie/ 100)
        Total += DepositoPeriodico 
        print("Money increasing yearly: ", round(Total,0))

# lets print the total amount of profit after the duration
print("After ", Duration, " years you will have this much money: ", round(Total,0))
print("You added this much money every Month / Year: ", DepositoPeriodico)
if YearlyOrMonthly == "M":
    print("In total you added this much money: ", DepositoPeriodico * Duration * 12)
    amountOfProfitFromInterestOnly = (Total - balanceInitial) - (DepositoPeriodico * Duration * 12)
else:
    print("In total you added this much money: ", DepositoPeriodico * Duration)
    amountOfProfitFromInterestOnly = (Total - balanceInitial) - (DepositoPeriodico * Duration)

print("That means you will have this much extra profit: ", amountOfProfitFromInterestOnly)
print("That means you will have this much extra profit in percentage: ", amountOfProfitFromInterestOnly / Total * 100, "%")
stop = time.time()
print("Time to run program: ", stop - start," seconds")