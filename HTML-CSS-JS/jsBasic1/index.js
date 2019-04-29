// document의 함수로 객체 가져오기
const title = document.getElementById("title");

// css 셀렉터와 비슷 #id, .class 이름으로 object 가져오기
const name = document.querySelector("#name");

// 텍스트 변경
title.innerText = "Bye javascript";
// 색변경
title.style.color = "black";
name.style.color = "#00FFFF";

// html문서의 타이틀 변경
document.title = "hi";
