const prompt = require('prompt-sync')({sigint: true});

console.log("Program to assign pet accessory")

const name = prompt('What is your name? ');
console.log(`Hey there ${name}`);

const pet = prompt(`What is your pet? ${name}? Enter C for cat, D for dog or X for no pet: `);

console.log("Suitable accessory: ");
if (pet == "C")
{
    console.log("Toy mouse");
}
else if (pet == "D")
{
    console.log("bone");
}
else
{
    console.log("It looks like you don't have a pet. Have you thought about the benefits?");
}


 