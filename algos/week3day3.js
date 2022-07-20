/* 
Given a SORTED array of integers, dedupe the array 
Because array elements are already in order, all duplicate values will be grouped together.
Ok to use a new array
Bonus: do it in O(n) time (no nested loops, new array ok)
Bonus: Do it in-place (no new array)
Bonus: Do it in-place in O(n) time and no new array
Bonus: Keep it O(n) time even if it is not sorted
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */

function dedupeSorted(nums) {
    for(var i = 0; i < nums.length; i++){
        if (nums[i] == nums[i+1]){
            nums.splice(i, 1) // .splice (the number you want to start at, the amount of numbers you want to splice or get rid of)
            i--;
        }
    }
    return nums
}

// Spensir's Way
// function dedupeSorted(nums) {
//     return [...new Set(nums)];
//     }


// Camden's Way
// function dedupeSorted(nums) {
//     let new_arr = []
//     for (let i = 0; i < nums.length; i++){
//         if (new_arr[new_arr.length-1] != nums[i]){
//             new_arr.push(nums[i])
//             // console.log(new_arr.includes([nums[i]]))
//             // console.log(new_arr)
//         }
//     }
//     return new_arr
// }

console.log(dedupeSorted(nums1));
console.log(dedupeSorted(nums2));
console.log(dedupeSorted(nums3));
console.log(dedupeSorted(nums4));


/*****************************************************************************/


/* 
Given an array of integers
return the first integer from the array that is not repeated anywhere else
If there are multiple non-repeated integers in the array,
the "first" one will be the one with the lowest index.
*/

const twoNums1 = [3, 5, 4, 3, 4, 6, 5];
const twoExpected1 = 6;

const twoNums2 = [3, 5, 5];
const twoExpected2 = 3;

const twoNums3 = [3, 3, 5];
const twoExpected3 = 5;

const twoNums4 = [5];
const twoExpected4 = 5;

const twoNums5 = [];
const twoExpected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */

// Did not solve it
// function firstNonRepeated(nums) {
    // var repeatedArr = [];
    // var non_repeat = 0;
//     for (var i = 0; i < nums.length; i++){
//         var non_repeat = nums[0];
//         for(var j = 0; j < nums.length; j++){
//             var x = false
//             if (nums[i] == nums[j]){
//                 non_repeat = nums[i+1];
//                 x = true
//             }
//         }
//         if (x = false){
//             var results = []
//             results.append(non_repeat)
//         }
//         return results[0]
//     }
// }

// Jesse's finished solution for ours
// function first_non_repeat(array){

//     var results = [];
//     var y = 0;
//     var non_repeat = array[y];

//     for (var i = 0; i < array.length; i++){

//         var x = false;

//         for (var j = 0; j < array.length; j++){

//             if (i != j){
//                 if (array[i] == array[j]){
//                     y++;
//                     x = true;
//                     non_repeat = array[y];

//                 }
//             }

//     }
//     if (x == false){
//         results.push(non_repeat);
//     }
// }
//     return results;
// }

function firstNonRepeated(nums){
    const freq = {}; // frequency table or hash map
            // key 
    for(const num of nums) {
        if(freq.hasOwnProperty(num)){
            freq[num]++;
        }
        else {
            freq[num] = 1;
        }
    }
    for (const num of nums) {
        if (freq[num] === 1){
            return num;
        }
    }
    return null
}

// Avery's Solution
// function firstNonRepeated(nums) {
//     let numObject = {};
//     let allLowestIndex = nums.length;
//     let lowestNoDupes = 0;

//     for(var i = nums.length-1; i >= 0; i--){
//         if(!(nums[i] in numObject)){
//             numObject[nums[i]] = { times: 1, lowestIndex: i};
//         }
//         else{
//             numObject[nums[i]].times++;
//             numObject[nums[i]].lowestIndex = i;
//         }
//     }
//     let isFound = false;

//     for(key in numObject){
//         number = numObject[key];
//         if(number.times == 1 && number.lowestIndex < allLowestIndex){
//             allLowestIndex = number.lowestIndex;
//             lowestNoDupes = +key;
//             isFound = true;
//         }
//     }
//     if(isFound == false){
//         return null
//     }

//     return lowestNoDupes
// }

console.log(firstNonRepeated(twoNums1))
console.log(firstNonRepeated(twoNums2))
console.log(firstNonRepeated(twoNums3))
console.log(firstNonRepeated(twoNums4))