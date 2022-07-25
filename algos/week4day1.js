/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */

// Mine & Michael's:
function recursiveSigma(num, i=1) {
    //Your code here
    //Santize value?
    //Base case?
    // var i = 1;
    // if (num < 0){
    //     return 0;
    // }
    // if (isNaN(num)){
    //     return null;
    // }
    // if (i === num){
    //     return num;
    // }
    // console.log(i);
    if (i > num){
        return 0;
    }
    return i + recursiveSigma(num, ++i)
    //Recursive call?
}

// Michael Stafford found another way to do it:
// function recursiveSigma(num) {
//     if (num <= 0) {
//         return 0
//     }
//     num = Math.floor(num)
//     return num + recursiveSigma(--num)
// }

// Tre's Solution
// function recursiveSigma(num, i=1) {
//     if (typeof num != "number") {
//         return ("INVALID DATA TYPE: " + typeof num)
//     }else if (i > num) {
//         return 0;
//     }
//     return i + recursiveSigma(num, i+1)
// }

// Brian's Solution
// function recursiveSigma(num) {
//     var rounded = Math.floor(num)

//     if(rounded <= 0) {
//         return 0
//     }
//     return rounded + recursiveSigma(--rounded)
    // return rounded + recursiveSigma(rounded - 1)
// }

console.log(recursiveSigma(num1)); // 15
console.log(recursiveSigma(num2)); // 3
console.log(recursiveSigma(num3)); // 0