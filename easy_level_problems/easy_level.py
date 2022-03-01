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


'''
    * 1672
    * You are given an m x n integer grid accounts where accounts[i][j] 
    * is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
    * Return the wealth that the richest customer has.

    * A customer's wealth is the amount of money they have in all their bank accounts. 
    * The richest customer is the customer that has the maximum wealth.

    * Example:

    * Input: accounts = [[1,2,3],[3,2,1]]
    * Output: 6
    * Explanation:
    * 1st customer has wealth = 1 + 2 + 3 = 6
    * 2nd customer has wealth = 3 + 2 + 1 = 6
    * Both customers are considered the richest with a wealth of 6 each, so return 6.
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            sumWealth = sum(customer)
            maxWealth = max(sumWealth, maxWealth)
        return maxWealth


'''
    * 2011
    * There is a programming language with only four operations and one variable X:

    * ++X and X++ increments the value of the variable X by 1.
    * --X and X-- decrements the value of the variable X by 1.
    * Initially, the value of X is 0.
    * Given an array of strings operations containing a list of operations, 
    * return the final value of X after performing all the operations.

    * Example:
    * Input: operations = ["--X","X++","X++"]
    * Output: 1
    * Explanation: The operations are performed as follows:
    * Initially, X = 0.
    * --X: X is decremented by 1, X =  0 - 1 = -1.
    * X++: X is incremented by 1, X = -1 + 1 =  0.
    * X++: X is incremented by 1, X =  0 + 1 =  1.
'''
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation == "--X" or operation == "X--": 
                x -= 1
            else:
                x += 1
        return x

'''
    * 2114
    
    * A sentence is a list of words that are separated by a single space 
    * with no leading or trailing spaces.
    * You are given an array of strings sentences, where each sentences[i] 
    * represents a single sentence.
    * Return the maximum number of words that appear in a single sentence.

    * Example:
    * Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    * Output: 6
    * Explanation: 
    * - The first sentence, "alice and bob love leetcode", has 5 words in total.
    * - The second sentence, "i think so too", has 4 words in total.
    * - The third sentence, "this is great thanks very much", has 6 words in total.
    * Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
'''
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWordCount = 1
        for sentence in sentences:
            maxWordCount = max(maxWordCount, sentence.count(" ") + 1)
        return maxWordCount

'''
    * 1470
    * Given the array nums consisting of 2n elements in the form 
    * [x1,x2,...,xn,y1,y2,...,yn].
    * Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    * Example:
    * Input: nums = [2,5,1,3,4,7], n = 3
    * Output: [2,3,5,4,1,7] 
    * Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Double list comprehension
        # A more readable solution was marginally slower on their machines
        # so to meet my goal of 50% faster, I used a list comprehension 
        return [num for i in range(n) for num in [nums[i], nums[i + n]]]


'''
    * 1512
    * Given an array of integers nums, return the number of good pairs.
    * A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    * Example 1:
    * Input: nums = [1,2,3,1,1,3]
    * Output: 4
    * Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    * Example 2:
    * Input: nums = [1,1,1,1]
    * Output: 6
    * Explanation: Each pair in the array are good.
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        keep dictionary, tracks if we've seen this number before
        if so, increment pair tracker accordingly 
        '''
        seenNums = {}
        goodPairs = 0
        for num in nums:
            if num in seenNums:
                goodPairs += seenNums[num]
                seenNums[num] += 1
            else:
                seenNums[num] = 1
        return goodPairs

'''
    * 1431
    * There are n kids with candies. You are given an integer array candies, 
    * where each candies[i] represents the number of candies the ith kid has, 
    * and an integer extraCandies, denoting the number of extra candies that you have.

    * Return a boolean array result of length n, where result[i] is true if, 
    * after giving the ith kid all the extraCandies, 
    * they will have the greatest number of candies among all the kids, or false otherwise.

    * Note that multiple kids can have the greatest number of candies.

    * Example:
    * Input: candies = [2,3,5,1,3], extraCandies = 3
    * Output: [true,true,true,false,true] 
    * Explanation: If you give all extraCandies to:
    * - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    * - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    * - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    * - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    * - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        maxKidCandyTracker = []
        for child in candies:
            maxKidCandyTracker.append(True if child + extraCandies >= maxCandies else False)
        return maxKidCandyTracker

'''
    * 1791
    * There is an undirected star graph consisting of n nodes labeled from 1 to n. 
    * A star graph is a graph where there is one center node and exactly n - 1 
    * edges that connect the center node with every other node.

    * You are given a 2D integer array edges where each 
    * edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
    * Return the center of the given star graph. 

    * Example
    *       4
    *       |
    *       2
    *      / \
    *     1   3
    * Input: edges = [[1,2],[2,3],[4,2]]
    * Output: 2
    * Explanation: As shown in the figure above, 
    * node 2 is connected to every other node, so 2 is the center.
'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        centerNode = 1
        seenEdges = {}
        for node1, node2 in edges:
            if node1 in seenEdges:
                seenEdges[node1] = seenEdges[node1] + 1
            else:
                seenEdges[node1] = 1
            if node2 in seenEdges:
                seenEdges[node2] = seenEdges[node2] + 1
            else:
                seenEdges[node2] = 1
            centerNode = node1 if seenEdges[node1] > seenEdges[node2] else node2
        return centerNode

'''
    * 1967
    * Given an array of strings patterns and a string word, 
    * return the number of strings in patterns that exist as a substring in word.
    * A substring is a contiguous sequence of characters within a string.

    * Example
    * Input: patterns = ["a","abc","bc","d"], word = "abc"
    * Output: 3
    * Explanation:
    * - "a" appears as a substring in "abc".
    * - "abc" appears as a substring in "abc".
    * - "bc" appears as a substring in "abc".
    * - "d" does not appear as a substring in "abc".
    * 3 of the strings in patterns appear as a substring in word.
'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        stringCount = 0
        for string in patterns:
            if word.find(string) != -1:
                stringCount += 1
        return stringCount

'''
    * 1450
    * Given two integer arrays startTime and endTime and given an integer queryTime.
    * The ith student started doing their homework at the time startTime[i] 
    * and finished it at time endTime[i].
    * Return the number of students doing their homework at time queryTime. 
    * More formally, return the number of students where queryTime lays 
    * in the interval [startTime[i], endTime[i]] inclusive.

    * Example
    * Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
    * Output: 1
    * Explanation: We have 3 students where:
    * The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
    * The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
    * The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
'''
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        busyStudents = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                busyStudents += 1
        return busyStudents

'''
    * 2057
    * Given a 0-indexed integer array nums, 
    * return the smallest index i of nums such that i mod 10 == nums[i], 
    * or -1 if such index does not exist.
    * x mod y denotes the remainder when x is divided by y.

    * Example
    * Input: nums = [0,1,2]
    * Output: 0
    * Explanation: 
    * i=0: 0 mod 10 = 0 == nums[0].
    * i=1: 1 mod 10 = 1 == nums[1].
    * i=2: 2 mod 10 = 2 == nums[2].
    * All indices have i mod 10 == nums[i], so we return the smallest index 0.
'''
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        smallestIndex = -1
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                smallestIndex = i
                break
        return smallestIndex

'''
    * 1200
    * Given an array of distinct integers arr, 
    * find all pairs of elements with the minimum absolute difference of any two elements.
    * Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    * a, b are from arr
    * a < b
    * b - a equals to the minimum absolute difference of any two elements in arr

    * Example
    * Input: arr = [4,2,1,3]
    * Output: [[1,2],[2,3],[3,4]]
    * Explanation: The minimum absolute difference is 1. 
    * List all pairs with difference equal to 1 in ascending order.
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arrCopy = sorted(arr)
        minAbsDiffPairs = [[arrCopy[0], arrCopy[1]]]
        minAbsDiff = abs(arrCopy[1] - arrCopy[0])
        for i in range(1, len(arrCopy) - 1):
            absoluteDiff = abs(arrCopy[i + 1] - arrCopy[i]) 
            if absoluteDiff <  minAbsDiff:
                minAbsDiffPairs = [[arrCopy[i], arrCopy[i + 1]]]
                minAbsDiff = absoluteDiff
            elif absoluteDiff == minAbsDiff:
                minAbsDiffPairs.append([arrCopy[i], arrCopy[i + 1]])
        return minAbsDiffPairs

'''
    * 2068
    * Two strings word1 and word2 are considered almost equivalent 
    * if the differences between the frequencies of each letter 
    * from 'a' to 'z' between word1 and word2 is at most 3.

    * Given two strings word1 and word2, each of length n, 
    * return true if word1 and word2 are almost equivalent, or false otherwise.

    * The frequency of a letter x is the number of times it occurs in the string.
    * Example
    * Input: word1 = "aaaa", word2 = "bccb"
    * Output: false
    * Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
    * The difference is 4, which is more than the allowed 3.
'''
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        wordCharTable = {}
        for char in word1:
            if char in wordCharTable:
                wordCharTable[char] += 1
            else:
                wordCharTable[char] = 1
        for char in word2:
            if char in wordCharTable:
                wordCharTable[char] -= 1
            else:
                wordCharTable[char] = -1
        for char in wordCharTable:
            if abs(wordCharTable[char]) > 3:
                return False
        return True

'''
    * 1408
    * Given an array of string words. 
    * Return all strings in words which is substring of another word in any order. 
    * String words[i] is substring of words[j], 
    * if can be obtained removing some characters to left and/or right side of words[j].

    * Example
    * Input: words = ["mass","as","hero","superhero"]
    * Output: ["as","hero"]
    * Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
    * ["hero","as"] is also a valid answer.
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subStrings = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j]:
                    word1 = words[i]
                    word2 = words[j]
                    if word1 in word2:
                        subStrings.add(word1)
        return list(subStrings)

'''
    * 412
    * Given an integer n, return a string array answer (1-indexed) where:
    * answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    * answer[i] == "Fizz" if i is divisible by 3.
    * answer[i] == "Buzz" if i is divisible by 5.
    * answer[i] == i (as a string) if none of the above conditions are true.

    * Example 1
    * Input: n = 3
    * Output: ["1","2","Fizz"]
    * Example 2
    * Input: n = 5
    * Output: ["1","2","Fizz","4","Buzz"]
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzArr = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                fizzBuzzArr.append("FizzBuzz")
            elif i % 5 == 0:
                fizzBuzzArr.append("Buzz")
            elif i % 3 == 0:
                fizzBuzzArr.append("Fizz")
            else:
                fizzBuzzArr.append(str(i))
        return fizzBuzzArr

'''
    * 2062
    * A substring is a contiguous (non-empty) sequence of characters within a string.
    * A vowel substring is a substring that only consists of vowels 
    * ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
    * Given a string word, return the number of vowel substrings in word.

    * Example
    * Input: word = "cuaieuouac"
    * Output: 7
    * Explanation: The vowel substrings of word are as follows (underlined):
    * - "uaieuo"
    * - "uaieuou"
    * - "uaieuoua"
    * - "aieuo"
    * - "aieuou"
    * - "aieuoua"
    * - "ieuoua"
'''
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowelStrCount = 0
        vowelSet = set(["a", "e", "i", "o", "u"])
        n = len(word)
        for i in range(n):
            char = word[i]
            if char in vowelSet:
                foundVowelsSet = set(char)
                foundVowels = {}
                foundVowels[char] = 1
                lastVowelIndex = i
                for j in range(i + 1, n):
                    if word[j] in vowelSet:
                        lastVowelIndex = j
                        rightChar = word[j]
                        foundVowelsSet.add(rightChar)
                        foundVowels[rightChar] = foundVowels[rightChar] + 1 if rightChar in foundVowels else 1
                    else:
                        break
                # once all vowels are found
                if len(foundVowelsSet) == 5:
                    vowelStrCount += 1
                    for k in range(lastVowelIndex, i, -1):
                        rightChar = word[k]
                        foundVowels[rightChar] -= 1
                        if foundVowels[rightChar] > 0:
                            vowelStrCount += 1
                        else:
                            break
        return vowelStrCount