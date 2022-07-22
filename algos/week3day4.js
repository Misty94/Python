/* 
Given an int to represent how much change is needed
calculate the fewest number of coins needed to create that change,
using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    let expected = {};
    let coins = [ 25, 10, 5, 1 ];
    let amount = cents;
    for( let i = 0; i < coins.length; i++ ) {
        while( amount >= coins[i] ) {
            if( i == 0 ) {
                if( !expected.hasOwnProperty('quarter') ) {
                    expected.quarter = 1;
                    amount = amount - coins[i];
                }
                else {
                    expected.quarter += 1;
                    amount = amount - coins[i];
                }
            }
            if( i == 1 ) {
                if( !expected.hasOwnProperty('dime') ) {
                    expected.dime = 1;
                    amount = amount - coins[i];
                }
                else {
                    expected.dime += 1;
                    amount = amount - coins[i];
                }
            }
            if( i == 2 ) {
                if( !expected.hasOwnProperty('nickel') ) {
                    expected.nickel = 1;
                    amount = amount - coins[i];
                }
                else {
                    expected.nickel += 1;
                    amount = amount - coins[i];
                }
            }
            if( i == 3 ) {
                if( !expected.hasOwnProperty('penny') ) {
                    expected.penny = 1;
                    amount = amount - coins[i];
                }
                else {
                    expected.penny += 1;
                    amount = amount - coins[i];
                }
            }
        }
    }
    return expected;
}

console.log( fewestCoinChange( cents1 ) );
console.log( fewestCoinChange( cents2 ) );
console.log( fewestCoinChange( cents3 ) );
console.log( fewestCoinChange( cents4 ) );

// function fewestCoinChange(cents) {

//     const centsDic = {
//         penny:0,
//         nickel:0,
//         dime:0,
//         quarter:0,
//     }

//     while(0 < cents){
//         if(cents >= 25){
//             centsDic.quarter += 1;
//             cents -= 25;
//             continue; 
//         }
//         if(cents >= 10){
//             centsDic.dime += 1;
//             cents -= 10;
//             continue; 
//         }
//         if(cents >= 5){
//             centsDic.nickel += 1;
//             cents -= 5;
//             continue; 
//         }
//         if(cents >= 1){
//             centsDic.penny += 1;
//             cents -= 1;
//             continue; 
//         }
//     }
//     return centsDic
// }

/* 
Missing Value
You are given an array of length N that contains, in no particular order,
integers from 0 to N . One integer value is missing.
Quickly determine and return the missing value.
*/

const twoNums1 = [3, 0, 1];
const twoExpected1 = 2;

const twoNums2 = [3, 0, 1, 2];
const twoExpected2 = null;
// Explanation: nothing is missing

/* 
Bonus: now the lowest value can now be any integer (including negatives),
instead of always being 0. 
*/

const twoNums3 = [2, -4, 0, -3, -2, 1];
const twoExpected3 = -1;

const twoNums4 = [5, 2, 7, 8, 4, 9, 3];
const twoExpected4 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {
    var missingvals = []
    var smallest = Math.min(...unorderedNums)
    var largest = Math.max(...unorderedNums)
    while(smallest != largest){
        if(!unorderedNums.includes(smallest + 1)){
            missingvals.push(smallest + 1)
        }
        smallest += 1
    }
    if( missingvals.length === 0 ) missingvals = null
    return missingvals
}

console.log(missingValue(twoNums1))
console.log(missingValue(twoNums2))
console.log(missingValue(twoNums3))
console.log(missingValue(twoNums4))

// function missingValue(unorderedNums) {
//     if (unorderedNums.length < 1) {
//     return null;
//     }

//     let min = unorderedNums[0];
//     let max = unorderedNums[0];
//     let actualSum = 0;

//     for (const n of unorderedNums) {
//     if (n < min) {
//         min = n;
//     }
//     if (n > max) {
//         max = n;
//     }
//     actualSum += n;
//     }

//     let expectedSum = 0;

//     for (let i = min; i <= max; i++) {
//     expectedSum += i;
//     }

//     console.log("ACT:", actualSum, "EXP:", expectedSum);

//     if (actualSum === expectedSum) {
//     return null;
//     }

//     return expectedSum - actualSum;
// }