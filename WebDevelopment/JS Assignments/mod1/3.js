var num1 = parseInt(prompt("input a number"));
var num2 = parseInt(prompt("input a second number"));
var num3 = parseInt(prompt("input a third number"));
var sum = num1 + num2 + num3
var product = num1 * num2 * num3
var average = sum / 3


document.querySelector("#welcome").innerHTML = `numbers: sum = ${sum}, product = ${product}, average = ${Math.round(average)} !`;