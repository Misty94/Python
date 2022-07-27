/*
Recursive Binary Search
Input: SORTED array of ints, int value
Output: bool representing if value is found
Recursively search to find if the value exists, do not loop over every element.
Approach:
Take the middle item and compare it to the given value.
Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
// Spencer's
function binarySearch(sortedNums, searchNum, left=0, right=sortedNums.length-1) { //will we need more parameters?
    //Your code here
    //Base case
    //primary logic
    //recursive call(s)
    if (left > right) {
        return false;
    }
    const mid = Math.floor((left + right) / 2);
    if (sortedNums[mid] === searchNum) {
        return true;
    }
    if (sortedNums[mid] > searchNum) {
        return binarySearch(sortedNums, searchNum, left, mid - 1);
    }
    return binarySearch(sortedNums, searchNum, mid + 1, right);
}

// Thiery's code
// function binarySearch(sortedNums, searchNum) {
    // console.log(sortedNums,"this is sorted nums")
    // let left_index = 0;
    // let right_index = sortedNums.length - 1;
    // while (left_index <= right_index) {
    //     let i = Math.floor(right_index - left_index / 2)
    //     if (sortedNums[i] == searchNum) {
    //         return true;
    //     }else if (sortedNums[i] > searchNum) {
    //         right_index = i-1;
    //     }else {
    //         left_index = i+1;
    //     }
    // }
    // return false;
//     let i = Math.floor((right_index - left_index) / 2)
//     if(sortedNums.length == 0){
//         return false;
//     }
//     if(sortedNums[i] == searchNum){
//         return true; 
//     }else if(sortedNums[i] > searchNum){
//         return binarySearch(sortedNums.slice(0,i),searchNum);
//     }else if(sortedNums[i] < searchNum ){
//         return binarySearch(sortedNums.slice(i+1),searchNum);
//     }
// }

// noah's and mine attempt (he was using slice but I guess I didn't type that out)
// function binarySearch(sortedNums, searchNum) { 
//     if (sortedNums.length < 0){
//         return false;
//     }
//     var half = Math.floor(sortedNums.length / 2)
//     if (searchNum == sortedNums[half] ) return true;
//     else if (searchNum > half){
//         return binarySearch(searchNum,)
//     }
// }

console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true
console.log(binarySearch(nums3, searchNum3)); // true