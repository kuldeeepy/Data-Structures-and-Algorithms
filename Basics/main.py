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


# (Q8) GCD or HCF

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


# (Q9) print something N times

def printNtimes(n):

    if n == 0: return
    print("Recursion!")
    printNtimes(n-1)

# printNtimes(5)


# (Q10) print name N times

def printNameN(i, n):
    if i >= n: return
    print("Hello, kuldeep!")
    printNameN(i+1, n)

# printNameN(0,5)


# (Q11) print 1 to N 

def print1ToN(n):
    if n == 0: return
    print1ToN(n-1)
    print(n)

# print1ToN(5)


# (Q12) print N to 1 

def printNTo1(n):
    if n == 0: return
    print(n)
    printNTo1(n-1)

# printNTo1(5)


# (Q13) print N to 1 

def sumOfN(n):
    if n == 0: return 0
    return n + sumOfN(n-1) 

# print(sumOfN(6))


# (Q14) factorial of a numb

def factorialOfN(n):
    if n == 0: return 1
    return n * factorialOfN(n-1)

# print(factorialOfN(3))


# (Q15) Reverse an array

# Approach 1 
def reverseArray(n, arr):
    p1, p2 = 0, n-1

    while (p1 < p2):
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1+=1
        p2-=1
    return arr

# print(reverseArray(5, [5,4,3,2,1]))

# Approach 2
def reverseArray2(start, end, arr):
    if (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray2(start+1, end-1, arr)
    return arr

# print(reverseArray2(0, 4, [5,4,3,2,1]))


# (Q16) Check palindrome (string)

# Approach 1
def checkPalindrom(string):
    p1, p2 = 0, len(string)-1

    while p1 < p2:
        if string[p1] !=  string[p2]:
            print("Not Palindrome")
            return
        p1 += 1
        p2 -= 1
    print("Palindrome")

# Approach 1
def checkPalindrom2(i, string):
    if i > len(string) //2:
        return True
    if string[i] != string[len(string)-i-1]:
        return False
    return checkPalindrom2(i+1, string)

# checkPalindrom("maam")
# print(checkPalindrom2(0, "racecar"))


# (Q17) fibonacci series upto N

# Approach 1 
def fibonacci(n):

    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib)
    
# Approach 2 
def fibonacci2(n):
    last = 0
    secondLast = 1
    print(last, secondLast, end=' ')

    for i in range(2, n+1):
        curr = last + secondLast
        last = secondLast
        secondLast = curr
        print(curr, end=' ')

# Approach 3
def fibonacci3(n, a=0, b=1):
    if a > n: 
        return
    print(a, end=" ")
    fibonacci3(n, b, a+b)

# fibonacci(6)
# fibonacci2(6)
# (fibonacci3(6))


# (Q18) count freq of array elements (int)

def countFreq(n, arr, target):
    hash = [0] * (n+1)

    for i in range(n):
        hash[arr[i]] += 1
    return hash[target]

# print(countFreq(5, [1,4,5,2,2]))


# (Q19) count freq of string elements (str)

def countFreq2(s, q):
    hash = [0] * 26

    for chr in s:
        hash[ord(chr) - ord('a')] += 1
    return hash[ord(q)-ord('a')]

# print(countFreq2("abcdabehf", 'h'))


# (Q20) Find the highest/lowest frequency element

def highLowFreq(arr):
    hash = {}

    for num in arr:
        hash[num] = hash.get(num, 0) +1
    max_freq = max(hash.values())
    min_freq = min(hash.values())

    max_val = [key for key, val in hash.items() if val == max_freq]
    min_val = [key for key, val in hash.items() if val == min_freq]
    print(*max_val, *min_val)

# highLowFreq([10, 5, 10, 15, 10, 5])

