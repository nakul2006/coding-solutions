# Concatenation of Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the  **concatenation**  of two `nums` arrays.

Return  *the array* `ans`.

 

 **Example 1:** 

```
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

 **Example 2:** 

```
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 1000
- 1 <= nums[i] <= 1000

## Solution

**Language:** C  
**Runtime:** 1 ms (beats 17.14%)  
**Memory:** 14.8 MB (beats 96.89%)  
**Submitted:** 2026-10-23T14:32:52.287Z  

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* ans=(int*)malloc(2*numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++){
        ans[i]=nums[i];
        ans[i+numsSize]=nums[i];
    }
    *returnSize = 2*numsSize;
    return ans;
}
```

---

[View on LeetCode](https://leetcode.com/problems/concatenation-of-array/)