/*console.log("script running!");

let name = 'Charlie'; //This is the name of the person
console.log('Hello ' + name + '!');

let age = 16; //this is the age of the person

if (age >= 18)
{
  console.log ('you are the Father!!!');
  //console.log(false);
}
else
{
  console.log ('you are not the Father!!!');
}
//console.log ('you are ' + age + ' years old!');
if (age < 18 && name === "John")
{

}
if(age < 18 || age > 80)
{

}

let raining = false;
if (!raining)
{
  console.log('Today is a sunny day');
}*/

///////resuable code////////
/*const greetPeople = (name1, name2) => {
  console.log('Hello, ' + name1 + ' and ' + name2 + '!');
}
const getFullName = (firstName, lastName) => {
  return firstName + ' ' + lastName;
}*/

//////using functions defined by others//////
/*let radius = 10;
let area = Math.PI * radius * radius;
radius = radius * 2;
area = Math.PI * Math.pow(radius, 2);
let width = Math.round(Math.random() * 100);
let height = Math.round(Math.random() * 50);
let circumference = width * 2 + height * 2;*/

//////function using global variables//////
let n = 1;
const increaseNumber = () => {
  n = n + 1;
  console.log(n);
}
setInterval(increaseNumber, 1000);
/// anonymous functions///
setInterval(() => {
  n = n + 1;
  console.log(n);
}, 1000);
