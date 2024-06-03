li_st = []
not_prime = True
amount_of_primes = 0
for i in range(2,1000000):
    li_st.append(str(i))
    not_prime = True
    for y in li_st:
        if int(y) != i:
            if i % int(y) == 0:
                not_prime = False
                break
    if not_prime == True:
        print(y)
        amount_of_primes +=1
print("Amount of primes:",amount_of_primes)
