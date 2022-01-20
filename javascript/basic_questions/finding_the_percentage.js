const input=require("readline-sync")
let len=input.questionInt("Enter the length of object =>  ")
let obj={}
for (let i=1;i<=len;i++){
    let name=input.question("Enter the name => ")
    // let marks=input.questionInt("Enter the len: ")
    let marks_array=[]
    for (let j=1;j<=3;j++){
        let m=input.questionInt("Enter the marks => ")
        marks_array.push(m)
    }
    obj[name]=marks_array

}
console.log(obj)
// console.log(obj.len())
let l=Object.keys(obj).length
// console.log(Object.keys(obj).length)

let average=[]
for (let k=0;k<2;k++){
    let sum=0
    let l=Object.values(obj)
    for (let i=0;i<Object.values(obj).length;i++){
        sum=sum+l[i]
    }
    average.push(sum)

}
console.log(average)