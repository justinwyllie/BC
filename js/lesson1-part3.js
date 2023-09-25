const prompt = require('prompt-sync')({sigint: true});

/**
 * 
 * @param {Array} ages - an array of numbers
 * @return {number} - the average of the numbers
 */
function calculateAverage(ages)
{
    let total = 0;
    let numberOfStudents = ages.length;

    for (let i = 0; i < numberOfStudents; i++)
    {   
        total = total + Number(studentAges[i]);
    }

    let averageAge = total / numberOfStudents;
    return Number(averageAge);
}

let input;
let studentAges = Array();

console.log("Enter an age or X to finish");

while (input !== "X")
{
    input = prompt('Enter age ');
    if (input !== "X")
    {
        studentAges.push(input);
    }
} 
let result = calculateAverage(studentAges);
console.log(`The average age of students in the class is: ${result}`)




 