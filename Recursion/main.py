
# (Q) Print numbers from 1 to N

def print_1_to_N(n):
    if n > 0:
        print_1_to_N(n-1)
        print(n)

# print_1_to_N(5)


# (Q) Print numbers from N to 1

def print_N_to_1(n):
     if n > 0:
        print(n)
        print_N_to_1(n-1)

# print_N_to_1(5)


# (Q) Factorial

def factorial(n):
    if n <= 0:
        return 1
    return factorial(n-1) * n
    
# print(factorial(5))    


# (Q) Fibonacci Sequence!

def fibonacci(n):
    
    if n == 0: return 0
    if n == 1: return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))


# (Q) Print Fibonacci Series!

def fibonacci_series(n, a=0, b=1):

    if a > n:
        return
    
    print(a, end=' ')
    fibonacci_series(n, b, a+b)

# fibonacci_series(20)


# (Q) Sum of Digits!

def sum_of_digits(nums):
    
    if nums < 9:
        return nums
    return sum_of_digits(nums // 10) + (nums % 10)

# print(sum_of_digits(1234))


# (Q) Reverse a String!

def reverse_string(str, idx=0):

    if idx == len(str):
        return ''
    return reverse_string(str, idx + 1) + str[idx]

# print(reverse_string('kuldeep'))


# (Q) Power Calculation!

def get_power(base, exp):

    if exp <= 0:
        return 1
    return get_power(base, exp-1) * (base)

# print(get_power(2,3))


# (Q) Array Sum!

def array_sum(arr, idx=0):

    if idx == len(arr):
        return 0
    return arr[idx] + array_sum(arr, idx+1)

# print(array_sum([1,2,3,4,5]))


# (Q) Palindrome Check!

def palindrome_check(str, idx=0):

    if idx == len(str):
        return ''
    rev_string = palindrome_check(str, idx+1) + str[idx]
    return rev_string

# print(palindrome_check('maam') == 'maam')  


# (Q) String Permutations!

def permute(string, l, r):

    if l == r:
        print(''.join(string))
    else:
        for i in range(l, r+1):
            string[l], string[i] = string[i], string[l]
            permute(string, l+1, r)
            string[l], string[i] = string[i], string[l]

# str = "abc"
# permute(list(str), 0, len(str)-1)


# (Q) Tower of Hanoi!

