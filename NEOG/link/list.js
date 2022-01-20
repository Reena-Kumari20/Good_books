array=[{name:"reena", age:11},{name:"anisha",age:20},{name:"sara",age:23}]
let i=0
while (i<array.length){
      console.log(array[i].name)
      console.log(array[i].age)
      if (array[i].age>12){
            console.log("have cycle age is greater then 12")
      }
      else{
            console.log("no cycle age is less then 12")
      }
      i++
}