// 1. Write a JavaScript program that accept two integers and display the larger.
const input=require("readline-sync")
let num1=input.questionInt("Enter the number1: ")
let num2=input.questionInt("Enter the number2: ")
if (num1>num2){
        console.log(`${num1} is larger`)
}
else if (num2>num1){
        console.log(`${num2} is larger`)
}
else{
        console.log(`Both number are equal`)
}