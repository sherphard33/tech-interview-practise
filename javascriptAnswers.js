// /*Two Number Sum
// Write a function that takes in a non-empty array of distinct intergers and an integer representing a target sum.
// If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no
// two numbers sum up to the targetSum , the function should return an empty array.
// */
// //array = [3, 5, -4, 8, 11, 1, 2, 6];
// //targetSum = 10;

// const twoNumSum = (arr, tSum) => {
//   const len = arr.length - 1;
//   let memo = {};
//   for (let i = 0; i < len; i++) {
//     let num1 = arr[i];
//     let num2 = tSum - num1;
//     if (num2 in memo) {
//       return [num1, num2];
//     } else {
//       memo[num1] = "another number";
//     }
//   }
//   return [];
// };

// /* Given two non empty arrays of integers, write a function that determines whether
// the second array is a subsequence of the first */

// //array = [5, 1, 22, 25, 6, -1, 8, 10];
// //sequence = [1, 6, -1, 10];

// const vailSeq = (arr, seq) => {
//   let idx = 0;
//   let len = arr.length;
//   for (let i = 0; i < len; i++) {
//     let value = arr[i];
//     if (idx == seq.length) {
//       return true;
//     }
//     let seqNum = seq[idx];
//     if (seqNum == value) {
//       idx++;
//     }
//   }
//   return idx == seq.length;
// };

// /*
// Write a function that takes in non-empty array of intergers that are sorted in ascending order and
// returns a new array of the same length with the squares of te original intergers also sorted in ascending order.
// */

// //array = [-4, -1, 5, 6, 8, 10, 22, 25];

// const array_sorter = (arr) => {
//   // Write your code here.
//   const len = arr.length;
//   const newArr = [];
//   for (let i = 0; i < len - 1; i++) {
//     let newValue = arr[i] ** 2;
//     newArr.push(newValue);
//   }
//   let sortedArray = newArr.sort(function (a, b) {
//     return a - b;
//   });
//   return sortedArray;
// };

// //Minimum waiting waiting time

// const minWaitingTime = (arr) => {
//   const len = arr.length;
//   let totalWaitingTime = 0;
//   arr.sort(function (a, b) {
//     return a - b;
//   });
//   for (let idx = 0; idx < len; idx++) {
//     let eRemaining = len - (idx + 1);
//     totalWaitingTime += arr[idx] * eRemaining;
//   }
//   return totalWaitingTime;
// };

// //array2 = [3, 2, 1, 2, 6];

const longArr = (arr) => {
  let memo = new Set();
  let sml = 0;
  let res = 0;
  for (let i = 0; i < arr.length; i++) {
    while (memo.has(arr.charAt(i))) {
      console.log("found dublicate", arr.charAt(i));
      memo.delete(arr.charAt(sml));
      sml++;
    }
    memo.add(arr[i]);
    //console.log("added next one", arr[i]);
    res = Math.max(res, i - sml + 1);
  }
  return res;
};
s = "abcabcbb";
console.log(longArr(s));
