const starbtn = document.querySelectorAll(".like-btn");

for (var i = 0; i < starbtn.length; i++) {
  starbtn[i].addEventListener("click", toglelike);
}

function toglelike(e) {
  if (this.childNodes[1].classList.contains("fa-solid")) {
    this.childNodes[1].classList.replace("fa-solid", "fa-regular");
  } else {
    this.childNodes[1].classList.replace("fa-regular", "fa-solid");
  }
}
