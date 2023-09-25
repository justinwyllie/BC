let studentAges = Array();
studentAges.push(10);
studentAges.push(12);   
studentAges.push(14);

let total = 0;
let numberOfStudents = studentAges.length;


for (let i = 0; i < numberOfStudents; i++)
{   
    total = total + Number(studentAges[i]);
}

let averageAge = total / numberOfStudents;
console.log(`The average age of students in the class is: ${averageAge}`);




 