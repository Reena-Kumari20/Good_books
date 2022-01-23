// Write a JavaScript conditional statement to find the sign of product of three numbers. Display an alert box with the specified sign
const input=require("readline-sync")
let num=input.questionInt("Enter the num: ")
let i=1
let m=1
while (i<=num){
        let num1=input.questionInt("Enter the number: ")
        m=m*num1
        i=i+1
}
if (m>=0){
        console.log(`+`)
}
else[
        console.log(`-`)
]
