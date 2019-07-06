/*
// 빈 파라미터 함수
() => console.log("hello world");

// 단일 파라미터 함수
id => console.log(id);

// 다중 파라미터 함수
function TestPrint(fisrt: string, second: string): string {
  return fisrt + " " + second;
}

console.log(TestPrint("first", "second"));

let TestPrint2 = (first: string, last: string) => first + " " + last;
console.log(TestPrint2("first", "second"));

// Optional이 아닌경우 반드시 파라미터가 필요, 맨 마지막에 선언
function TestOptional(title: string, length?: number) {}

// Default 파라미터가 없으면 설정된 값으로 할당
function TestDefault(title: string, length: number = 300) {}

// Rest 가변길이 파라미터 전달 -> 배열로 사용가능
function TestRest(title: string, ...numArray: number[]) {}
let rest = new TestRest("title", 1, 2, 3, 4, 5);
*/

// 함수 오버로드 , 구현은 하나만
function Add(str: string, str2: string): string;
function Add(num: number, num2: number): number;
function Add(prop: any, prop2: any): any {
  if (typeof prop == "string") {
    return prop + prop2 + " 문자열 더하기";
  } else if (typeof prop == "number") {
    return prop + prop2 + " 숫자 더하기";
  }

  return "오류";
}

console.log("Add(1, 2) :", Add(1, 2));
console.log('Add("1", "2") :', Add("1", "2"));
