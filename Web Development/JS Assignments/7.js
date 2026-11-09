var rolls = parseInt(prompt("how many throws?"));

function RollDie(cnt) {
    let num = 0;
    for (let i = 0; i <= cnt; i++) {
        num += Math.floor(Math.random() * 6);
        console.log(num)
    }
    return num;
}
var rolltotal = RollDie(rolls);
document.querySelector("#roll").innerHTML = `you rolled ${rolls} times and got ${rolltotal} total!`;