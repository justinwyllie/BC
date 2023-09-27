const prompt = require('prompt-sync')({sigint: true});
let class4B = new Array();

console.log(typeof class4B);

console.log("Enter student names and X when finished")
let studentName = '';

while (studentName != 'X')
    {
        studentName = prompt("Enter name: ")  
        class4B.push(studentName)
    }

numberStudents = class4B.length;

console.log(`There are now ${numberStudents} students in Class 4B`);
