numdie = parseInt(prompt("How many dice to roll ?"))
sum = parseInt(prompt("What should the total be ?"))

sums = 0;
proc = 0;
for(let i = 0; i < 10000; i++){
    for(let i = 0; i < numdie; i++){
        sums += Math.floor(Math.random() *6)+1;
    }
    if(sums === sum){
        proc++;
    }
    sums = 0
}
document.getElementById("prob").innerText=`Chance to get ${sum} with ${numdie} dice is ${Math.round(Number.parseFloat(proc / 100))}%`