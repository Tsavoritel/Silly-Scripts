"use strict";

let timerID = null;

function removeBox(evt){
    //Get parent element
    let boxParent = evt.currentTarget.parentElement;
    boxParent.removeChild(evt.currentTarget);
}

function timedAction(){
   let boxDiv = document.querySelector(".box");
   let newParagraph = document.createElement("p");

   newParagraph.innerText = "I am a box!!!";
   //newParagraph.className = "div-green";
   newParagraph.setAttribute("class", "div-green");
   newParagraph.addEventListener("click", removeBox);

   boxDiv.appendChild(newParagraph);
   console.log(boxDiv.clientHeight)
   if (boxDiv.clientHeight > 750) {
    console.log("end game !!")
   }
}

function startBoxing(){
    console.log("Starting making boxes...")
    timerID = setInterval(timedAction, 2000);
}

function endBoxing() {
    console.log("Stopping making boxes...")
    clearInterval(timerID);
}


let startButton = document.querySelector("#start");
let endButton = document.querySelector("#end");

startButton.addEventListener("click", startBoxing);
endButton.addEventListener("click", endBoxing);

let header = document.querySelector("#main-header");
header.innerText = "Page about Boxes";



let alsoHeader = document.getElementById("main-header");
console.log(alsoHeader);

let paragraphs = document.querySelectorAll("p");
console.log(paragraphs);

let paragraphsToo = document.getElementsByTagName("p");
console.log(paragraphsToo);