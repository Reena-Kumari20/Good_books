const input=require("readline-sync")
const num=input.questionInt("Enter the number: => ")
let string = "";
for (let i = 1; i <= num; i++) {
  for (let j = 0; j < i; j++) {
    string += "*";
  }
  string += "\n";
}
console.log(string);