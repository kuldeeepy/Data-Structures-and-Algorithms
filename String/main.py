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


# (Q6) Group Anagrams

# Approach 1 
def groupAnagrams(strs):
    group = {}
    
    for word in strs:
        key = "".join(sorted(word))
        if key not in group:
            group[key] = [word]
        else:
            group[key].append(word)
    return list(group.values())

# Approach 2 
# from collections import defaultdict
def groupAnagrams(strs):
    map = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        map[tuple(count)].append(s)
    return list(map.values())

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# (Q6) Remove Outermost Parentheses

def removeOuterParanthesis(s):
    res, count = [], 0

    for p in s:
        if p == '(' and count != 0: res.append(p)
        if p == ')' and count > 1: res.append(p)
        count += 1 if p == '(' else -1
    return "".join(res)

# print(removeOuterParanthesis("(()())(())"))


# (Q6) Largest Odd Number in String

def largestOddNumb(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""
    
# print(largestOddNumb("4206"))


# (Q7) Longest Common Prefix

def longestCommonPrefix(strs):
    if not strs: return ""

    res = strs[0]
    for word in strs[1:]:
        temp = ""
        for i in range(min(len(res), len(word))):
            if res[i] == word[i]:
                temp += res[i]
            else:
                break
        res = temp
    return res if res else ""

# print(longestCommonPrefix(["dog","racecar","car"]))


# (Q7) Rotate String

def rotateString(s, goal):
    if len(s) != len(goal): return False
    modified_s = s
    modified_s += s
    if goal in modified_s:
        return True 
    return False

# print(rotateString("abcde", "abced"))


# (Q8) Valid Anagram

def isAnagram(s,t):
    if len(s) != len(t): return False
    map = {}

    # first string 
    for chr in s:
        if chr in map: map[chr] += 1
        else: map[chr] = 1

    # second string
    for chr in t:
        if chr in map: 
            map[chr] -= 1
            if map[chr] == 0: del map[chr]
        else: return False
    return len(map) == 0

# print(isAnagram("anagram", "nagaram"))


# (Q9) Sort Characters By Frequency

def frequencySort(s):
    if not s: return s

    map = {}
    for chr in s:
        if chr in map: map[chr] += 1
        else: map[chr] = 1
    items = list(map.items())
    for i in range(len(items)):
        for j in range(0, len(items)-i-1):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    string = ""
    for k,v in items:
        string += k*v
    return string

# print(frequencySort("tree"))


# (Q10) Count of Distinct Substring

def countSubstr(s):
    seen = set()
    start, count = 0, 0

    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        count += (end-start +1)
    return count

# print(countSubstr('aabcb'))


# (Q11) subsequ relation betwn 2 strs

def verifyString(s,t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        j += 1
    return i == len(s)

# print(verifyString("axc", "ahbgdc"))


# (Q12) Reverse words in string

# Approach 1 TC: O(n) SC: O(n)
def reverseWords(string, n):
    def reverseNow(chars, res):
        strg = ""
        for i in range(len(chars)-1,-1,-1):
            strg += chars[i]
        res.append(strg)

    res = []
    temp_str = string.split()
    for word in temp_str:
        reverseNow(word, res)
    return res

# Approach 1 TC: 
def reverseWords2(string, n):
    return string

# print(reverseWords2("hello world", 11))


# (Q13) Longest substring without repeat chars

# Approach 1 TC: O(n^3) SC: O(n)
def lengthOfLongestSubstr(s):
    def isUnique(string):
        chrSet = set()
        for chr in string:
            chrSet.add(chr)
        return string == "".join(chrSet)

    mxSubstr = 0
    for i in range(len(s)):
        substr = ""
        for j in range(i,len(s)):
            substr += s[j]
            if isUnique(substr) and len(substr) > mxSubstr:
                mxSubstr = len(substr)
    return mxSubstr

# Approach 1 TC: O(n) SC: O(miin(n,strs))
def lengthOfLongestSubstr2(s):
    left = maxLen = 0
    charSet = set()
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        maxLen = max(maxLen, (right-left)+1)
    return maxLen

# print(lengthOfLongestSubstr("abcabcbb"))


# (Q14) Permutation in String

# Approach 1 TC: SC:
def checkInclusion(s1,s2):
    left = 0
    str = ""
    for right in range(len(s2)):
        while s2[right] == s1[left]:
            str += s2[right]
            left += 1
        else:
            break
    return [s1, str]
    
print(checkInclusion("ab","eidbaooo"))