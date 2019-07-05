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
// 클래스 일반적인 객체지향 언어와 비슷
// 명시하지 않을 경우 기본은 public
var News = /** @class */ (function () {
    function News() {
        this.author = "ESPN";
    }
    News.prototype.format = function () {
        return this.newsTitle + " : " + this.channelNum + " by " + this.author;
    };
    return News;
}());
var espn = new News();
espn.channelNum = 1;
espn.newsTitle = 'NFL Today';
console.log(espn.format());
// 상속관계에서만 사용 가능한 protected
var base = /** @class */ (function () {
    function base() {
    }
    return base;
}());
var child = /** @class */ (function (_super) {
    __extends(child, _super);
    function child() {
        return _super !== null && _super.apply(this, arguments) || this;
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
