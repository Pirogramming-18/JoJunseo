let secondText = document.getElementById('second')
let milliText = document.getElementById('milli')

let startBtn = document.getElementById('startBtn')
let stopBtn = document.getElementById('stopBtn')
let resetBtn = document.getElementById('resetBtn')

let second = parseInt(secondText.innerText)
let milli = parseInt(milliText.innerText)

let timer 

let timerOn = false;

function printTime(){
    milli++;
    document.getElementById('milli').innerText = milli;
    if(milli==99){
        second++;
        milli = 0;
        document.getElementById('second').innerText = second;
    }
}

function startTimer(){
    if(!timerOn){
        timer = setInterval(printTime,10)
        timerOn = true
    }
}

function stopTimer(){
    if(timerOn){
        clearInterval(timer)
        timerOn=false
    }
}

function resetTimer(){
    if(!timerOn){
    milli = 0
    second = 0
    document.getElementById('milli').innerText = milli;
    document.getElementById('second').innerText = second;
}
}

startBtn.addEventListener('click', startTimer)
stopBtn.addEventListener('click', stopTimer)
resetBtn.addEventListener('click', resetTimer)



