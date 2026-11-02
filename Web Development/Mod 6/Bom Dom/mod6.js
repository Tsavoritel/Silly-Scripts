/* i do not know why this is called ENA, im just following along
the following allows you to make an update functon basically */
"use strict";

function removeBox(evt) {
    let boxParent = evt.currentTarget.parentElement;
    boxParent.removeChild(evt.currentTarget);
}

function timedAction(){
    let boxDiv = document.querySelector(".box");
    let newParagraph = document.createElement("p");

    newParagraph.innerText = "I am a box !!"
    //newParagraph.className = "div-green" OR
    newParagraph.setAttribute("class", "div-green")
    newParagraph.addEventListener("click", removeBox)

    boxDiv.appendChild(newParagraph);

    console.log("Time !!")
}

function startBoxing() {
    console.log("Starting making boxes...")
    timerID = setInterval(timedAction, 2000)
}

function endBoxing() {
    console.log("Stopped making boxes...")
    clearInterval(timerID);
}

console.dir(document);

/* BOM allows you to call certain meta methods*/

/* DOM does this: */
let header = document.querySelector("#mh");
header.innerText = "Page about Boxes"
console.log(header)

let boxDiv = document.querySelector(".box")
let htmlP = "<p>Example</p>"
boxDiv.innerHTML = htmlP;

let paragraphs = document.querySelectorAll("p")
console.log(paragraphs);