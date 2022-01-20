// Create a function called shortcut to remove all the lowercase vowels in a given string.

// Examples
// "hello"     -->  "hll"
// "codewars"  -->  "cdwrs"
// "goodbye"   -->  "gdby"
// "HELLO"     -->  "HELLO"

let input = require("readline-sync");
var str= input.question("Enter your string:  ")
function shortcut (string) {
      let str1=""
     for (let i=0;i<string.length;i++){
        if (string[i] == "a" || string[i] == "e" || string[i] == "i" || string[i]== "o" || string[i] == "u") {
          i++
        }
        else{
            str1=str1+string[i]
        }
      }
      return str1;
}
console.log(shortcut(str))