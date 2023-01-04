let secondText = document.getElementById("second");
let milliText = document.getElementById("milli");

let startBtn = document.getElementById("startBtn");
let stopBtn = document.getElementById("stopBtn");
let resetBtn = document.getElementById("resetBtn");

let deleteBtn = document.querySelector("#record-menu button");
let recordCheck = document.querySelector("#record-menu input");

let second = parseInt(secondText.innerText);
let milli = parseInt(milliText.innerText);

let records = document.getElementById("records");

let timer;

let timerOn = false;

function recordTime() {
  const newRecord = document.createElement("div");
  newRecord.classList.add("record");

  const newCheck = document.createElement("input");
  newCheck.setAttribute("type", "checkbox");
  newRecord.appendChild(newCheck);

  const newTimebox = document.createElement("div");
  newTimebox.classList.add("record-time-box");

  const newSecond = document.createElement("p");
  newSecond.classList.add("record-second");
  newSecond.innerText = second.toString().padStart(2, "0");
  newTimebox.appendChild(newSecond);

  const newColon = document.createElement("p");
  newColon.innerHTML = ":";
  newTimebox.appendChild(newColon);

  const newMilli = document.createElement("p");
  newMilli.classList.add("record-milli");
  newMilli.innerText = milli.toString().padStart(2, "0");
  console.log();
  newTimebox.appendChild(newMilli);

  newRecord.appendChild(newTimebox);

  records.appendChild(newRecord);
}

function printTime() {
  milli++;
  document.getElementById("milli").innerText = milli
    .toString()
    .padStart(2, "0");
  if (milli == 99) {
    second++;
    milli = 0;
    document.getElementById("second").innerText = second
      .toString()
      .padStart(2, "0");
  }
}

function startTimer() {
  if (!timerOn) {
    timer = setInterval(printTime, 10);
    timerOn = true;
  }
}

function stopTimer() {
  if (timerOn) {
    clearInterval(timer);
    timerOn = false;
    recordTime();
  }
}

function resetTimer() {
  if (!timerOn) {
    milli = 0;
    second = 0;
    document.getElementById("milli").innerText = "00";
    document.getElementById("second").innerText = "00";
  }
}

function deleteRecord() {
  const findRecord = document.querySelectorAll(".record");
  findRecord.forEach((element) => {
    if (element.children[0].checked) {
      element.remove();
    }
  });
  recordCheck.checked = false;
}

function selectAll() {
  if (recordCheck.checked) {
    const findCheckRecord = document.querySelectorAll(".record");
    findCheckRecord.forEach((element) => {
      element.children[0].checked = true;
    });
    console.log("checked");
  } else {
    const findCheckRecord = document.querySelectorAll(".record");
    findCheckRecord.forEach((element) => {
      element.children[0].checked = false;
    });
    console.log("unchecked");
  }
}

startBtn.addEventListener("click", startTimer);
stopBtn.addEventListener("click", stopTimer);
resetBtn.addEventListener("click", resetTimer);
deleteBtn.addEventListener("click", deleteRecord);
recordCheck.addEventListener("click", selectAll);
