//2
function showTime() {
    let now = new Date();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    console.log(`${minutes}:${seconds}`);
}

//3
let count = 0;
let interval = setInterval(() => {
    console.log(count);
    count++;
    if (count > 15) {
        clearInterval(interval); // აჩერებს setInterval-ს 15-ის შემდეგ
    }
}, 500);

//4
setTimeout(() => console.log(2), 1000); 
setTimeout(() => console.log(1), 2000); 
setTimeout(() => console.log(3), 3000);