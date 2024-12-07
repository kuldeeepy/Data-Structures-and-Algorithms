# (Q1) Top K Frequent Elements

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


# (Q2) Product of Array Except Self

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


# (Q3) Longest Consecutive Sequence

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


# (Q4) 3Sum

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


# (Q5) Container With Most Water

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


# (Q6) Trapping Rain Water

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

# print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))


# (Q7)  Equillibrium element

# Approach 1 TC: O(n^2) SC: O(1)
def equilEl(arr):
    for i in range(1,len(arr)-1):
        leftSum = rightSum = arr[i]

        for j in range(i):
            leftSum += arr[j]

        for k in range(i+1, len(arr)):
            rightSum += arr[k]
        
        if leftSum == rightSum:
            return i
    return -1

# Approach 2 TC: O(n) SC: O(1)
def equilEl2(arr):
    return arr

# print(equilEl2([15,1,5,5,5]))
# print(equilEl2([1,2,3]))


# (Q8) Rotate the array by K 

# TC: O(n) SC: O(1) 
def rotateByK(arr, k):
    def reverseArr(nums, start, end):
        while start < end:
            nums[start], arr[end] = nums[end], arr[start]
            start += 1 
            end -= 1
        return nums

    k = k % len(arr)
    reverseArr(arr, 0, len(arr)-1)
    reverseArr(arr, 0, k-1)
    reverseArr(arr, k, len(arr)-1)
    return arr

# print(rotateByK([1,2,3,4,5,6,7],3))


# (Q8) Sum of subarray II

# Approach 1 TC: O(n^2) SC: O(1)
def sumOfSubarrayII(arr,k):
    for i in range(len(arr)):
        sum_subarr = 0
        for j in range(i,len(arr)):
            sum_subarr += arr[j]
            if sum_subarr == k:
                return True
    return False

# Approach 2 TC: O(n) SC: O(n)
def sumOfSubarrayII2(arr, k):
    prefix, currSum = set([0]), 0

    for n in arr:
        currSum += n
        if currSum - k in prefix:
            return True
        else:
            prefix.add(currSum)
    return False

# print(sumOfSubarrayII2([1,2,1,3,4], 3))


# (Q9) Maximum subarray

# Approach 1 TC: O(n^2) SC: O(1)
def maxSubArr(arr):
    mxSub = 0
    for i in range(len(arr)):
        sum_subarr = 0
        for j in range(i,len(arr)):
            sum_subarr += arr[j]
            mxSub = max(sum_subarr, mxSub)
    return mxSub

# Approach 2 TC: O(n) SC: O(1)
def maxSubArr2(arr):
    mxSum = arr[0]
    currSum = arr[0]

    for i in range(1,len(arr)):
        currSum = max(arr[i], currSum + arr[i])
        mxSum = max(currSum, mxSum)
    return mxSum

# print(maxSubArr2([1, 2, 0, 4, 5]))

# (Q10) Max product subarray

# Approach 1 TC: O(n^2) SC: O(1)
def maxProdSubarr(arr):
    res = arr[0]
    for i in range(len(arr)-1):
        prod = arr[i]
        for j in range(i+1, len(arr)):
            res = max(res, prod)
            prod *= arr[j]
        res = max(res, prod)
    return res

# Approach 2 TC: O(n) SC: O(1)
def maxProdSubarr2(arr):
    mxProd = res = arr[0]
    for i in range(1,len(arr)):
        mxProd = max(arr[i], mxProd * arr[i])
        res = max(res, mxProd)
    return res

# print(maxProdSubarr2([4,5,-1,2]))


# (Q11) subarray sum equal to K

# Approach 1 TC: O(n^2) SC: O(1)
def subarraySumToK(nums,k):
    count = 0
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i,len(nums)):
            sub_sum += nums[j]
            if sub_sum == k:
                count += 1
    return count

# Approach 2 TC: O(n) SC: O(1) (works on positive nums)
def subarraySumToK2(nums,k): 
    sum = i = count = 0
    for j in range(len(nums)):
        sum += nums[j]
        while sum > k and i <= j:
            sum -= nums[i]
            i += 1
        if sum == k:
            count += 1
    return count

# Approach 3 TC: O(n) SC: O(n) (works on all)
def subarraySumToK3(nums,k):
    pref_sum_count = {0:1}
    sum = count = 0
    for num in nums:
        sum += num
        if sum - k in pref_sum_count:
            count += pref_sum_count[sum-k]
        pref_sum_count[sum] = pref_sum_count.get(sum, 0)+1
    return count

# print(subarraySumToK3([1,2,3],3))


# (Q12) subarraySum less than M

# Approach 1 TC: O(n^2) SC: O(1) 
def subarrSumLessThanM(nums, k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum < k: count += 1
    return count

# Approach 2 TC: O(n) SC: O(1) 
def subarrSumLessThanM2(nums, k):
    left = sum = count = 0
    for right in range(len(nums)):
        sum += nums[right]
        while sum >= k:
            sum -= nums[left]
            left += 1
        count += (right-left)+1
    return count

# print(subarrSumLessThanM2([1,5,1,3,2], 5))


# (Q12) Best Time to Buy and Sell Stock

def maxProfit(nums):
    profit = 0
    left, right = 0, 1

    while right < len(nums):
        if nums[left] < nums[right]:
            profit = max(profit, nums[right]-nums[left])
        else:
            left = right
        right += 1
    return profit

# print(maxProfit([7,1,5,3,6,4]))

# (Q13) Best Time to Buy and Sell Stock II

# Approach 1 TC: O(n^2) SC: O(1)
def maxProfitII(nums):
    profit = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                profit += nums[j]-nums[i]
            break
    return profit

# Approach 1 TC: O(n) SC: O(1)
def maxProfitII2(nums):
    profit = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            profit += nums[i] - nums[i-1]
    return profit

# print(maxProfitII2([7,1,5,3,6,4]))


# (Q14) Subarry Product less than K

# Approach 1 TC: O(n^2) SC: O(1)
def subarrayProdLessThanK(nums,k):
    count = 0
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            prod *= nums[j]
            if prod < k:
                count += 1
    return count

# Approach 1 TC: O(n) SC: O(1)
def subarrayProdLessThanK2(nums,k):
    if k <= 1: return 0
    count = left = right = 0
    prod = 1
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k and left <= right:
            prod //= nums[left]
            left += 1
        count += (right-left)+1
    return count

# print(subarrayProdLessThanK([10,5,2,6],100))


# (Q14) Weight Lifting

def weightLift(nums):
    harry = john = 0
    flag, weight = True, 0
    a, z = 0, len(nums)-1
    while a <= z:
        curr_lift = 0
        if flag:
            while a <= z and curr_lift <= weight:
                curr_lift += nums[a]
                a += 1
            harry += curr_lift
            flag = False
        else:
            while a <= z and curr_lift <= weight:
                curr_lift += nums[z]
                z -= 1
            john += curr_lift
            flag = True
        weight = curr_lift
    return [harry, john]

# print(weightLift([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))