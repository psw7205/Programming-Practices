/*
클래스 일반적인 객체지향 언어와 비슷
명시하지 않을 경우 기본은 public
생성자의 이름은 constructor로 고정
컴파일 시 클래스는 함수로 작성됨
생성자나 속성 선언시 초기화를 하지 않는 경우 속성이 undefined일 수 있음
-> 타입에러, 확실히 문제 없다고 생각하는 경우 변수 명 뒤에 !를 붙여 해결

*/
class News {
    constructor(title: string, num: number) {
        this.newsTitle = title;
        this.channelNum = num;
    }
    public newsTitle: string;
    public channelNum: number;
    private author: string = "ESPN";

    format(): string {
        return `${this.newsTitle} : ${this.channelNum} by ${this.author}`;
    }
}

let espn = new News("Today News", 1);
console.log(espn.format());

// 생성자에서 프로퍼티 생성, 할당
class News2 {
    private author: string = "ESPN";
    constructor(public newsTitle: string, public channelNum: number) {}
    format(): string {
        return `${this.newsTitle} : ${this.channelNum} by ${this.author}`;
    }
}

let espn2 = new News2("Today News", 1);
console.log(espn2.format());

class GetterSetter {
    private _value!: string;
    public get GetValue(): string {
        return this._value;
    }
    public set SetValue(v: string) {
        if (v != "") this._value = v;
    }
}

// static 정적 변수, 메소드는 클래스 이름으로 공유
class Counter {
    static cnt: number = 0;

    static CountIncrease() {
        Counter.cnt += 1;
    }
    GetCount(): number {
        return Counter.cnt;
    }
}

let cnt = new Counter();
let cnt2 = new Counter();
console.log("cnt :", cnt.GetCount());
console.log("cnt2 :", cnt2.GetCount());

// cnt2.increaseCount(); // 불가능
Counter.cnt = 10;
Counter.CountIncrease();
Counter.CountIncrease();
console.log("cnt :", cnt.GetCount());
console.log("cnt2 :", cnt2.GetCount());

// 상속관계에서만 사용 가능한 protected
// 부모의 생성자는 super()로 호출
class base {
    protected id: number;
    constructor(num: number) {
        this.id = num;
    }
}

class child extends base {
    name: string;
    constructor(str: string, num: number) {
        super(num);
        this.name = str;
    }

    print(): string {
        return `${this.name} id is ${this.id}`;
    }
}

// readonly 변수 선언 시 또는 생성자에서만 할당 가능
class HelloWorld {
    readonly name: string = "park sang woo";

    changeName() {
        // name = 'tmp'; // readonly이기 때문에 쓰기 불가능
    }
}
