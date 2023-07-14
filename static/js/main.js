// 예방 대처법 버튼1, 버튼2, 버튼3 클릭할 때마다 각각의 버튼에 맞는 요소로 변경

// 먼저 default로 버튼1의 정보이어야 하므로 이렇게 구현함
var num = 1;
if (num == 1) {
  document.getElementById("text").innerText = "누군가 뒤따라오고 있어요!";
  document.getElementById("orangebox").innerText = "빠르게 걸어야하나?";
  document.getElementById("whitebox").innerText = "소리를 질러야하나?";
  num++;
}

// 버튼 1을 클릭했을 때, 정보 출력
var button1 = document.getElementById("button1");

function btn1Click() {
  document.getElementById("text").innerText = "누군가 뒤따라오고 있어요!";
  document.getElementById("orangebox").innerText = "빠르게 걸어야하나?";
  document.getElementById("whitebox").innerText = "소리를 질러야하나?";
  document.getElementById("button1").style.backgroundColor = "#fe9738";
  document.getElementById("button2").style.backgroundColor = "#d9d9d9";
  document.getElementById("button3").style.backgroundColor = "#d9d9d9";
}

// 버튼 2를 클릭했을 때, 정보 출력
var button2 = document.getElementById("button2");

function btn2Click() {
  document.getElementById("text").innerText = "누군가 문을 두드려요!";
  document.getElementById("orangebox").innerText = "문을 열어야 하나?";
  document.getElementById("whitebox").innerText = "신고를 해야 하나?";
  document.getElementById("button1").style.backgroundColor = "#d9d9d9";
  document.getElementById("button2").style.backgroundColor = "#fe9738";
  document.getElementById("button3").style.backgroundColor = "#d9d9d9";
}

// 버튼 3을 클릭했을 때, 정보 출력
var button3 = document.getElementById("button3");

function btn3Click() {
  document.getElementById("text").innerText = "모르는 사람이 도촬을 해요!";
  document.getElementById("orangebox").innerText = "핸드폰을 뺏어야 하나?";
  document.getElementById("whitebox").innerText = "소리를 질러야 하나?";
  document.getElementById("button1").style.backgroundColor = "#d9d9d9";
  document.getElementById("button2").style.backgroundColor = "#d9d9d9";
  document.getElementById("button3").style.backgroundColor = "#fe9738";
}
// 사이렌 버튼 누르면 사이렌 소리 나오도록
const myAudio = new Audio();
myAudio.src = "media/siren.mp3"; // 실제 mp3 파일의 경로를 지정해주세요

var btnPlay = document.getElementById("siren_btn");
var isSirenOn = false;

function toggleSirenBtnBackground() {
  if (isSirenOn) {
    myAudio.play();
  } else {
    myAudio.pause();
  }
  isSirenOn = !isSirenOn;
}

btnPlay.addEventListener("click", toggleSirenBtnBackground);
btnPlay.addEventListener("click", toggleSirenBtnBackground);