/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
// function reverseString(str) {
//     //Your code here
//     return str.split("").reverse().join(""); //.join = creates & returns a new string
//     // str.split("") - turns the string into an array
//     // for(var i = 0; i < str.length; i++){
//     //     var temp = 
//     // }
    
// }

function reverseString(str) {
    var newstr = "";
    for (var x = str.length-1; x >= 0; x--){
        newstr += str[x];
    }
    return newstr;
}

// function reverseString(str) {
//     reversed = "";
//     for (let i = 0; i < str.length; i++) {
//         reversed = str[i] + reversed;
//     }
//     return reversed
// }

// function reverseString(str) {
//     var splitString = str.split("")
//     var reverseArray = splitString.reverse()
//     var joinArray = reverseArray.join("")
//     return joinArray
// }


//TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str5 = "object oriented programming";
const expected5 = "OOP";

// The 4 pillars of OOP
const str6 = "abstraction polymorphism inheritance encapsulation";
const expected6 = "APIE";

const str7 = "software development life cycle";
const expected7 = "SDLC";

// Bonus: ignore extra spaces
const str8= "  global       information tracker    ";
const expected8 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
// function acronymize(str) {
//     //Your code here
//     var newstr = "";
//     var array = str.split(" ");
//     for(var i = 0; i < array.length; i++){
//         if (array[i].length > 0){
//             newstr += array[i][0]
//         }
//     }

//     return newstr.toUpperCase();
// }

function acronymize(str) {
    //Your code here
    var newstr = "";
    var array = str.split(" ");
    for(var i = 0; i < array.length; i++){
        if (array[i] != ""){
            newstr += array[i][0];
        }
    }

    return newstr.toUpperCase();
}

// //TEST CODE FOR ACRONYMIZE
console.log(acronymize(str5)) // Expected: OOP
console.log(acronymize(str6)) // Expected: APIE
console.log(acronymize(str7)) // Expected: SDLC
//BONUS TEST CASE
console.log(acronymize(str8)) // Expected: GIT