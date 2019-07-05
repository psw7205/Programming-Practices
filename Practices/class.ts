// 클래스 일반적인 객체지향 언어와 비슷
// 명시하지 않을 경우 기본은 public
// 컴파일 시 클래스는 함수로 작성됨
class News {
    public newsTitle: string;
    public channelNum: number;
    private author: string = "ESPN";

    format(): string {
        return `${this.newsTitle} : ${this.channelNum} by ${this.author}`;
    }
}

let espn = new News();
espn.channelNum = 1;
espn.newsTitle = 'NFL Today';

console.log(espn.format());

// 상속관계에서만 사용 가능한 protected
class base {
    protected id: number;
}

class child extends base {
    name: string;
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