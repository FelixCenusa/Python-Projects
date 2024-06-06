import time
start = time.time()
print("Hello world")
balanceInitial = 20000
DepositoPeriodico = 10000
IntresAnual = 1.10
Inflatie = 1.03
Duracion = 60
Total = balanceInitial

variable = 0
InteresAnualConInflatie = IntresAnual - Inflatie + 1
print(chr(27) + "[2J" + chr(27) + "[;H")
while (variable < Duracion):
    variable+= 1

    Total += DepositoPeriodico 
    Total *= InteresAnualConInflatie
    print(round(Total,0))
print("Dupa ", Duracion, " ani o sa ai atati bani: ", round(Total,0))
print("Adica atata procent extra: ", ((Total - balanceInitial) - (DepositoPeriodico * Duracion)) / balanceInitial * 100, "%")
print("Total cummulative interest: ", round((IntresAnual - Inflatie)  * Duracion * 100), "%")
print("Total compound interest" , round(InteresAnualConInflatie ** Duracion * 100), "%")
print("Amount compounded compared to just adding the apr: ", (((Total - balanceInitial) - (DepositoPeriodico * Duracion)) / balanceInitial * 100) - ((IntresAnual - Inflatie)  * Duracion * 100), "%")
end = time.time()
totalTime = end - start
print("Time to run proogram", totalTime)