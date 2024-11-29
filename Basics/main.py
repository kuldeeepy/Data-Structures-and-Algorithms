# Pattern Printing 

# (Q1)

# * * * * 
# * * * * 
# * * * * 
# * * * * 
# * * * * 

def print1(n):
    for i in range(n):
        for j in range(n):
            print("*",  end=" ")
        print()

# print1(4)

# (Q2)

# * 
# * * 
# * * * 
# * * * * 

def print2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=' ')
        print()

# print2(4)

# (Q3)

# 1
# 1 2 
# 1 2 3 
# 1 2 3 4

def print4(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

# print4(4) 

# (Q4)

# * * * * *
# * * * *
# * * *
# * * 
# * 

def print5(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j, end=" ")
        print()

# print5(5)

# (Q6)

def print6(n):
    for i in range(n):
        # space 
        for a in range(n-i-1):
            print(" ",end = " ")
        # star 
        for b in range(2*i+1):
            print("*", end=" ")
        # space 
        for c in range(n-i-1):
            print(" ",end = " ")
        print()

# print6(5)

# (Q7) 

def print6(n):
    for i in range(n):
        # space 
        for a in range(i):
            print(" ",end = " ")
        # star 
        for b in range(2*n-(2*i+1)):
            print("*", end=" ")
        # space 
        for c in range(i):
            print(" ",end = " ")
        print()

# print6(5)

# (Q8) 

def print8(n):
    # Top half
    for i in range(n):
        # Spaces
        for a in range(n - i - 1):
            print(" ", end=" ")
        # Stars
        for b in range(2 * i + 1):
            print("*", end=" ")
        print()

    # Bottom half
    for i in range(n - 2, -1, -1):
        # Spaces
        for a in range(n - i - 1):
            print(" ", end=" ")
        # Stars
        for b in range(2 * i + 1):
            print("*", end=" ")
        print()

# print8(8)


# (Q9) 

def print9(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=' ')
        print()
    for k in range(n):
        for l in range(1,n-k+1):
            print("*", end=" ")
        print()

# print9(6)

# (Q10) 

def print10(n):
    val = None
    for i in range(1,n+1):
        val = 1 if i % 2 != 0 else 0
        for j in range(1,i+1):
            print(val, end=" ")
            val = 1 - val
        print()

# print10(5)

# (Q11) 

def print11(n):
    for i in range(1, n + 1):
        for a in range(1, i + 1):
            print(a, end=" ")

        for b in range(2 * (n - i)):
            print(" ", end=" ")

        for c in range(i, 0, -1):  
            print(c, end=" ")
        print()  

# print11(5)

# Basic Maths (playing with numbers)

# (Q1) Extract all the values of nums

def extractVals(n):
    while (n > 0):
        digit = n % 10
        print(digit)
        n = n // 10

# extractVals(7789)

# (Q2) Count digits in a numb

def countDigs(n):
    count = 0

    while (n > 0):
        count +=1
        n = n // 10
    return count

# print(countDigs(7789))

# (Q3) Reverse nums

def reverseNs(n):
    revNums = 0

    while (n > 0):
        digit = n % 10
        revNums = (revNums * 10) + digit
        n = n // 10
    return revNums

# print(reverseNs(7789))


# (Q4) Chek palindrom

def pal(n):
    rev  = 0
    dup = n

    while (n > 0):
        lastDig = n % 10
        rev = (rev * 10) + lastDig
        n = n // 10
    return dup == rev

# print(pal(7789))


# (Q5) Armstrong Nums

def armStrongNums(n):
    num_len = len(str(n))
    dupl = n
    sum = 0

    while (n > 0):
        lastDig = n % 10
        sum += lastDig ** num_len
        n = n // 10
    return sum == dupl

# print(armStrongNums(371))


# (Q6) Print Divisors

# In O(n) of TC
def printDivisors(n):
    for i in range(1, n+1):
        if (n % i == 0):
            print(i,end=' ')
    print()

def printDivisors2(n):
    arr = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            arr.append(i)
            if n // i != i:
                arr.append(n//i)
    print(*sorted(arr))

# printDivisors(36)
# printDivisors2(36)


# (Q7) Check for Prime

def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if (n % i == 0):
            count += 1
    return count == 2

# print(isPrime(17))


# (Q7) GCD or HCF

# Approach 1 
def GcdHcf(n1, n2):
    gcd = 0

    for i in range(min(n1, n2), 0,-1):
        if n1 % i == 0 and n2 % i == 0:
            print(i)
            break

def GcdHcf2(n1, n2):
    while (n1 > 0 and n2 > 0):
        if n1 > n2: n1 = n1 % n2
        else: n2 = n2 % n1

    if n1 == 0: return n2
    return n1

# GcdHcf(20, 40)
# print(GcdHcf2(20, 40))