//1

const currentDate = new Date();
console.log(currentDate)

//2
console.log(currentDate.getFullYear());
console.log(currentDate.getMonth() + 1); 
console.log(currentDate.getDate());
console.log(currentDate.getHours());


let timerInterval;
let elapsedTime = 0;
let running = false;

const timerDisplay = document.getElementById('timer');
const startStopBtn = document.getElementById('startStopBtn');

startStopBtn.addEventListener('click', () => {
    if (running) {
        clearInterval(timerInterval);
        startStopBtn.textContent = 'დაწყება';
    } else {
        const startTime = Date.now() - elapsedTime;
        timerInterval = setInterval(() => {
            elapsedTime = Date.now() - startTime;
            timerDisplay.textContent = formatTime(elapsedTime);
        }, 1000);
        startStopBtn.textContent = 'შეჩერება';
    }
    running = !running;
});

function formatTime(ms) {
    const totalSeconds = Math.floor(ms / 1000);
    const hours = String(Math.floor(totalSeconds / 3600)).padStart(2, '0');
    const minutes = String(Math.floor((totalSeconds % 3600) / 60)).padStart(2, '0');
    const seconds = String(totalSeconds % 60).padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}