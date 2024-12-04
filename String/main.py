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

# (Q10) Top K Frequent Elements

# Approach 1 
def topKFrequent(nums, k):
    map, arr, res = {}, [], []
    for num in nums:
        if num in map: map[num] += 1
        else: map[num] = 1

    for num,cnt in map.items():
        arr.append([cnt,num])
    arr.sort()
    
    while len(res) < k:
        res.append(arr.pop()[1])
    return res

# Approach 2
def topKFrequent2(nums, k):
    map, res = {}, []
    freq = [[] for _ in range(len(nums)+1)]
    for num in nums:
        if num in map: map[num] += 1
        else: map[num] = 1

    for num,cnt in map.items():
        freq[cnt].append(num)

    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]: res.append(n)
        if len(res) == k: return res

# print(topKFrequent2([1,1,1,2,2,3], 2))


# (Q11) Product of Array Except Self

# Approach 1 TC O(n^2)
def productExceptSelf(nums):
    res = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                prod *= nums[j]
        res.append(prod)
    return res

# Approach 2 TC O(n)
def productExceptSelf2(nums):
    res = [0] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

# print(productExceptSelf2([1,2,3,4]))


# (Q12) Longest Consecutive Sequence

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for num in nums:
        if (num-1) not in numSet:
            length = 0
            while (num+length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

# print(longestConsecutive([100,4,200,1,3,2]))


# (Q12) 3Sum

# Approach 1 O(n^3)
def threeSum(nums):
    res = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    res.add(tuple(tmp))
    return [list(i) for i in res]

# Approach 2 O(n^2)
def threeSum2(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0: 
                r -= 1
            elif sum < 0: 
                l += 1
            else: 
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
    return res

# print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum2([1,-1,-1,0]))


# (Q13) Container With Most Water

# Approach 1 O(n^2)
def maxArea(height):
    res = []
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            bth = j - i
            hth = min(height[i], height[j])
            area = bth * hth
        res.append(area)
    return max(res)

# Approach 2 O(n)
def maxArea2(height):
    l, r = 0, len(height)-1
    water = 0
    while l < r:
        bth = r - l
        hth = min(height[l], height[r])
        area = bth * hth
        water = max(water, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return water

# print(maxArea2([1,8,6,2,5,4,8,3,7]))


# (Q14) Trapping Rain Water

# Approach 1 TC: O(n^2) SC: O(1)
def trap(height):
    totalWater = 0
    for i in range(len(height)):
        leftMax = rightMax = height[i]

        for a in range(i):
            leftMax = max(leftMax, height[a])

        for b in range(i+1, len(height)):
            rightMax = max(rightMax, height[b])
        totalWater += min(leftMax, rightMax) - height[i]
    return totalWater

# Approach 1 TC: O(n) SC: O(1)
def trap2(height):
    return height

print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap2([4,2,0,3,2,5]))