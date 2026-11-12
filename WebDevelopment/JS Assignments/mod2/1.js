num = prompt("Input an integer.");
prime = false;
divisible = false;

for (let i = 2; i <= num/2; i++) {
    console.log(`${num}/${i}=${num/i}`);
    if (Number.isInteger(num / i) && num !== i) {
        divisible = true;
        console.log("triggered")
    }
}
if (!divisible) {
    prime = true;
}
document.querySelector("#prime").innerHTML = `${num} is prime: ${prime}`;