// var 호이스팅 O
// let, const 호이스팅 X
// const를 기본적으로 쓰고, 재할당이 반드시 필요한 변수만 let을 이용해 선언
// 변수 타입: number, string, boolean
// let<변수명>: <타입명> = <값>;
let num: number = 1;
console.log("num :", num);

let str: string = "string";
console.log("str :", str);

//[](array)
let arrNum: number[] = [1, 2, 3];
let strNum: string[] = ["ABC", "DEF", "EFG"];
console.log("arrNum :", arrNum);
console.log("strNum :", strNum);

//tuple
let tup: [number, string] = [25, "박상우"];
console.log("tuple :", tup);
// any 어느 자료형이든 할당 가능, 타입검사 X
let item: any = 1;
item = true;
item = "string";

// void 함수 반환 시 값이 없는 경우
// null, undefined

// 유니온 타입
let val: number | string; //number 또는 string타입 할당 가능
val = 1;
val = "string";

// enum
enum Color {
    Red,
    Green,
    Blue
}

let color: Color = Color.Green;
