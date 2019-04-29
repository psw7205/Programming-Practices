//let은 변수 변경 가능, const는 상수 변경 불가능

let a = 10;
console.log(a);
a = 20;
console.log(a);

const b = 20;
// b = 30; // 실행 X
console.log(b);

console.log("-------------------------------------------------");

// array
const ar = [1, 2, 3, 4, 5];

console.log(ar);

console.log("-------------------------------------------------");

const info = {
  name: "park",
  age: 25,
  gender: "male"
};

console.log(info);

// const이지만 값은 변경 가능
info.age = 26;
console.log(info.age);

// object 자체는 변경 불가
// info = {
//   name: "asd",
//   age: 12,
//   gender: "asd"
// };

console.log("-------------------------------------------------");

// 콘솔은 어떤 object일까...?
console.log(console);

console.log("-------------------------------------------------");

// 함수 function funcName (pram1, ...) { ... }
// 문자열의 연결은 ,도 가능하고 +로도 가능
function sayHello(name, age) {
  console.log("hello", name, "// age : " + age);
}
sayHello("psw", 26);

//함수 return
//`` 을 사용한 { }로 스트링 사용하기
function sayHello2(name, age) {
  return `hello ${name} // age : ${age}`;
}
const sayPSW = sayHello2("psw", 26);
console.log(sayPSW);

console.log("-------------------------------------------------");

const cal = {
  plus: function(x, y) {
    return x + y;
  },
  minus: function(x, y) {
    return x - y;
  }
};

console.log(cal.plus(1, 2));
console.log(cal.minus(3, 1));
