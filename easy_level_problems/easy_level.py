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
'''
class Solution:
    def interpret(self, command: str) -> str:
        

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