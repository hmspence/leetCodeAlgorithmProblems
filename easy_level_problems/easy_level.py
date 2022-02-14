'''
    * This file contains 'Easy' problems from Leetcode
    * My criteria is each solution is at least faster than 50% of all user submissions
'''

'''
    * 1678. Goal Parser Interpretation
    * 
    * You own a Goal Parser that can interpret a string command. 
    * The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
    * The Goal Parser will interpret "G" as the string "G", "()" as the string "o", 
    * and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
    * Given the string command, return the Goal Parser's interpretation of command.
    * 
    * Example 1:
    * Input: command = "G()(al)"
    * Output: "Goal"
    * Explanation: The Goal Parser interprets the command as follows:
    * G -> G
    * () -> o
    * (al) -> al
    * The final concatenated result is "Goal".
    * 
    * Engineer Notes:
    * I could not make the solution fast enough without Python's native 'replace' function
    * A more scalable and readable solution would perform slower on Leetcode
    * 
'''
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

'''
    * 1720. Decode XORed Array
    * 
    * There is a hidden integer array arr that consists of n non-negative integers.
    * It was encoded into another integer array encoded of length n - 1, 
    * such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], 
    * then encoded = [1,2,3].
    * You are given the encoded array. You are also given an integer first, 
    * that is the first element of arr, i.e. arr[0].
    * Return the original array arr. It can be proved that the answer exists and is unique.
    * 
    * Example 1:
    * Input: encoded = [1,2,3], first = 1
    * Output: [1,0,2,1]
    * Explanation: If arr = [1,0,2,1], then first = 1 
    * and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
    *
    * Engineer Explanation:
    * XOR is an 'exclusive or' bitwise operator
    * We are provided with the first value of the original array,
    * so for the first value, we simply need to add that to the returned array.
    * Then, stepping through the encoded array, perform the bitwise operation 
    *  37: 0 0 1 0 0 1 0 1
    * ^23: 0 0 0 1 0 1 1 1
    * _____________________
    *  50  0 0 1 1 0 0 1 0
    * XOR checks if only one digit is 1
'''
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])
        return arr

'''
    * 1342 Number of Steps to Reduce a Number to Zero
    * 
    * Given a non-negative integer num, return the number of steps to reduce it to zero. 
    * If the current number is even, you have to divide it by 2, otherwise, 
    * you have to subtract 1 from it.
    *
    * Example 1:
    * Input: num = 14
    * Output: 6
    * Explanation:
    * Step 1) 14 is even; divide by 2 and obtain 7.
    * Step 2) 7 is odd; subtract 1 and obtain 6.
    * Step 3) 6 is even; divide by 2 and obtain 3.
    * Step 4) 3 is odd; subtract 1 and obtain 2.
    * Step 5) 2 is even; divide by 2 and obtain 1.
    * Step 6) 1 is odd; subtract 1 and obtain 0.
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            steps += 1
            if num % 2:
                num -= 1
            else:
                num /= 2
        return steps

'''
    * 1920
    * Given a zero-based permutation nums (0-indexed), 
    * build an array ans of the same length where ans[i] = nums[nums[i]] 
    * for each 0 <= i < nums.length and return it.

    * A zero-based permutation nums is an array of distinct integers 
    * from 0 to nums.length - 1 (inclusive).

    * Input: nums = [5,0,1,2,3,4]
    * Output: [4,5,0,1,2,3]
    * Explanation: The array ans is built as follows:
    * ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], 
    * nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    * = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    * = [4,5,0,1,2,3]
'''
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # List comprenhension builds our array for us
        return [nums[nums[index]] for index in range(len(nums))]


'''
    * 1929
    * Given an integer array nums of length n, you want to create 
    * an array ans of length 2n where ans[i] == nums[i] 
    * and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    * Specifically, ans is the concatenation of two nums arrays.
    * Return the array ans.

    * Example 1:

    * Input: nums = [1,2,1]
    * Output: [1,2,1,1,2,1]
    * Explanation: The array ans is formed as follows:
    * - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
    * - ans = [1,2,1,1,2,1]
'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [num for num in nums] + [num for num in nums]

'''
    * 1480
    * Given an array nums. We define a running sum of an array as 
    * runningSum[i] = sum(nums[0]…nums[i]).

    * Return the running sum of nums.
    * Example:

    * Input: nums = [1,2,3,4]
    * Output: [1,3,6,10]
    * Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSums = [nums[0]]
        for i in range(1, len(nums)):
            runningSums.append(nums[i] + runningSums[i - 1])
        return runningSums