# (Q1) Reverse words of a string 

def reverseWords(s):
    stack, word = [], ""
    for char in s.strip():
        if char == " ":
            if word:
                stack.append(word)
                word = ""
        else:
            word += char
    if word: stack.append(word)

    res = ""
    while stack:
        res += stack.pop()
        if stack: res += " "
    return res

# print(reverseWords("a good   example"))


# (Q2) Longest Palindrome in a string

# Approach 1 (Brute Force) 
def longestPalSubstr(s):

    def isPalindromic(subs):
        l, r = 0, len(subs)-1

        while l < r:
            if subs[l] != subs[r]:
                return False
            l += 1
            r -= 1
        return True
    
    substring = ""
    for i in range(len(s)):
        substr = ""
        for j in range(i, len(s)):
            substr += s[j]
            if isPalindromic(substr):
                if len(substring) < len(substr):
                    substring = substr
    return substring

# Approach 2 (Expand around center alg) 
def longestPalSubstr2(s):

    def expand_around_center(l,r):
        longest_pald = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(longest_pald):
                longest_pald = s[l:r+1]
            l -= 1
            r += 1
        return longest_pald

    longest_susbtr = s[0]

    for i in range(len(s)):
        # odd length palindrome 
        odd_pald = expand_around_center(i, i)
        if len(odd_pald) > len(longest_susbtr):
            longest_susbtr = odd_pald

        #  even length palindrome 
        even_pald = expand_around_center(i,i+1)
        if len(even_pald) > len(longest_susbtr):
            longest_susbtr = even_pald
    return longest_susbtr

# print(longestPalSubstr2("babad"))


# (Q3) Roman Number to Integer and vice versa

def romanToInt(s):
    sum = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            sum -= roman[s[i]]
        else:
            sum += roman[s[i]]
    return sum + roman[s[-1]]

# print(romanToInt("MCMXCIV"))


# (Q4) Implement ATOI/STRSTR

def myAtoi(s):
    MAX_INT, MIN_INT = 2**31-1, -2**31
    i, n = 0, len(s)

    # skipping leading spaces
    while i < n and s[i] == " ":
        i += 1

    # checking for sign
    sign = 1
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    #converting to int
    res = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        #check number range
        if res > (MAX_INT - digit) // 10:
            return MAX_INT if sign == 1 else MIN_INT
        res = res * 10 + digit
        i += 1
    return res * sign

# print(myAtoi("0-1"))


# (Q5) Find Words That Can Be Formed by Chars
def countChars(words, chars):
    map = {}

    for chr in chars:
        if chr in map: map[chr] += 1
        else: map[chr] = 1
        
    count = 0
    for word in words:
        temp_map = map.copy()
        can_form = True
        for chr in word:
            if chr not in temp_map or temp_map[chr] == 0:
                can_form = False
                break
            temp_map[chr] -= 1
        if can_form: count += len(word)
    return count

# print(countChars(["cat","bt","hat","tree"], "atach"))


# (Q6) Second Largest Digit in a String

def secondHighest(s):
    digits = {int(char) for char in s if char.isdigit()}
    if len(digits) < 2: return -1
    return sorted(digits, reverse=True)[1]

# print(secondHighest("dfa12321afd"))
# print(secondHighest("abc1111"))