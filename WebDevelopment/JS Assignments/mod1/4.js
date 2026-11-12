//import { usrname } from "2.js"
console.log(`username is ${usrname}`)
num = Math.floor(Math.random() * 4);
house = "";
if (num === 1) {
    house = "Gryffindor";
}
else if (num === 2) {
    house = "Hufflepuff";
}
else if (num === 3) {
    house = "Ravenclaw";
}
else {
    house = "Slytherin";
}

document.querySelector("#house").innerHTML = `${usrname}, you are ${house} !`;