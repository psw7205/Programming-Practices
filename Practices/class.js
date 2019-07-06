"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
/*
클래스 일반적인 객체지향 언어와 비슷
명시하지 않을 경우 기본은 public
생성자의 이름은 constructor로 고정
컴파일 시 클래스는 함수로 작성됨
생성자나 속성 선언시 초기화를 하지 않는 경우 속성이 undefined일 수 있음
-> 타입에러, 확실히 문제 없다고 생각하는 경우 변수 명 뒤에 !를 붙여 해결

*/
var News = /** @class */ (function () {
    function News(title, num) {
        this.author = "ESPN";
        this.newsTitle = title;
        this.channelNum = num;
    }
    News.prototype.format = function () {
        return this.newsTitle + " : " + this.channelNum + " by " + this.author;
    };
    return News;
}());
var espn = new News("Today News", 1);
console.log(espn.format());
// 생성자에서 프로퍼티 생성, 할당
var News2 = /** @class */ (function () {
    function News2(newsTitle, channelNum) {
        this.newsTitle = newsTitle;
        this.channelNum = channelNum;
        this.author = "ESPN";
    }
    News2.prototype.format = function () {
        return this.newsTitle + " : " + this.channelNum + " by " + this.author;
    };
    return News2;
}());
var espn2 = new News2("Today News", 1);
console.log(espn2.format());
var GetterSetter = /** @class */ (function () {
    function GetterSetter() {
    }
    Object.defineProperty(GetterSetter.prototype, "GetValue", {
        get: function () {
            return this._value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GetterSetter.prototype, "SetValue", {
        set: function (v) {
            if (v != "")
                this._value = v;
        },
        enumerable: true,
        configurable: true
    });
    return GetterSetter;
}());
// static 정적 변수, 메소드는 클래스 이름으로 공유
var Counter = /** @class */ (function () {
    function Counter() {
    }
    Counter.CountIncrease = function () {
        Counter.cnt += 1;
    };
    Counter.prototype.GetCount = function () {
        return Counter.cnt;
    };
    Counter.cnt = 0;
    return Counter;
}());
var cnt = new Counter();
var cnt2 = new Counter();
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
var base = /** @class */ (function () {
    function base(num) {
        this.id = num;
    }
    return base;
}());
var child = /** @class */ (function (_super) {
    __extends(child, _super);
    function child(str, num) {
        var _this = _super.call(this, num) || this;
        _this.name = str;
        return _this;
    }
    child.prototype.print = function () {
        return this.name + " id is " + this.id;
    };
    return child;
}(base));
// readonly 변수 선언 시 또는 생성자에서만 할당 가능
var HelloWorld = /** @class */ (function () {
    function HelloWorld() {
        this.name = "park sang woo";
    }
    HelloWorld.prototype.changeName = function () {
        // name = 'tmp'; // readonly이기 때문에 쓰기 불가능
    };
    return HelloWorld;
}());
