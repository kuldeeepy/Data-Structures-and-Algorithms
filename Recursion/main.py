
# (Q) Factorial of N

def fact(n):
    if n <= 1:
        return n
    return fact(n-1) * n

# print(fact(5))

# (Q) Fibonacci sequence

def fib(n,memo):
    
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
        
    memo[n] = fib(n-2, memo) + fib(n-1, memo)
    return memo[n]

# print(fib(6,{}))

# (Q) Sum of digits

def sum(n):
    if n <= 9:
        return n
    return sum(n//10) + (n%10)

# print(sum(1234))

# (Q) Power of n

def pow(a,b):
    if b == 0:
        return 1
    return pow(a,b-1) * a

# print(pow(2,4))

# (Q) Reverse string

def reverse(s, n):
    if n == 0:
        return ''
    return s[n-1] + reverse(s,n-1) 

# print(reverse('hello', len('hello')))

# (Q) Chek palindrome

def palindrome(string, i):

    if i >= len(string) // 2:
        return True
    
    if string[i] != string[len(string) - i - 1]:
        return False
    return palindrome(string, i+1)

# print(palindrome('radar',0))
# print(palindrome('hello',0))

# (Q) Greatest Common Divisor (GCD)

def get_GCD(a,b):
    if b == 0:
        return a
    return get_GCD(b , a % b)

# print(get_GCD(48,18))