const prompt = require('prompt-sync')({sigint: true});

let classAges = [];

function averageAge(ages)
{
    let total = 0;
    ages.forEach((age) =>
    {
        total = total + age;
    })
    return total / ages.length;
}

const className = prompt("Enter name of class: ")  

inputAge = ''

while (inputAge != 'X')
{
    inputAge = prompt("Enter age of students one by one and press X when finished: ")  
    if (inputAge != 'X')
    {
        inputAge = parseInt(inputAge);
        classAges.push(inputAge);
    }
       
}
    

result = averageAge(classAges)
console.log(`The average age of students in ${className} is ${result}`);
