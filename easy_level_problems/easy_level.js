/**
 * This file contains 'Easy' problems from Leetcode
 * My criteria is each solution is at least faster than 50% of all user submissions
 */

/**
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
 * At the time of submission, this solution was 86% faster with less memory than 72%
 * Most solutions hard-code in checking for each char, I think this one is more scalable. 
 * 
 * @param {string} command
 * @return {string}
 */
const interpret = (command) => {
  const dict = { G: 'G', '()': 'o', '(al)': 'al', '': '' };
  const specialChars = new Set(['(', 'a', 'l']);
  let translated = '';
  let i = 0;
  while (i < command.length) {
    const char = command[i];
    if (char === ')') {
      const o = i - 1 >= 0 ? command.slice(i - 1, i + 1) : '';
      const al = i - 3 >= 0 ? command.slice(i - 3, i + 1) : '';
      translated = translated + (dict[o] || dict[al]);
    } else if (char === 'G') {
      translated = translated + dict[char];
    }
    i++;
  }
  return translated;
};

 /**
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
  * 
  * @param {number[]} encoded
  * @param {number} first
  * @return {number[]}
  */
const decode = (encoded, first) => {
  const arr = [first];
  encoded.forEach((ele, i) => {
    arr[i + 1] = ele ^ arr[i];
  });
  return arr;
};

 /**
  * 1342. Number of Steps to Reduce a Number to Zero
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
  * 
  * @param {number} num
  * @return {number}
  */
const numberOfSteps = (num) => {
  let steps = 0;
  while (num > 0) {
    steps = steps + 1;
    if (num % 2) {
      num = num - 1;
    } else {
      num = num / 2;
    }
  }
  return steps;
};

/**
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
 */
var buildArray = function (nums) {
  const builtArray = [];
  for (let i = 0; i < nums.length; i++) {
    builtArray.push(nums[nums[i]]);
  }
  return builtArray;
};

/**
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
 */
var getConcatenation = function (nums) {
  return nums.map((num) => num).concat(nums.map((num) => num));
};