interface comparable {
	public boolean compareTo(Object o); // 인터페이스는 모두가 퍼블릭이여야 함
}

interface drawable {
	public static final int MAX = 100;

	public void colorDraw();
}

class MyMouse implements drawable, comparable { // 인터페이스는 여러개 구현 가능
	public void colorDraw() {
	}

	public boolean compareTo(Object o) {
		return false;
	} // 인터페이스는 무조건 구현해줘야 함
}

abstract class abstractShape {
	// 추상메소드를 하나라도 가지고 있다면 추상클래스가 됨
	// 오직 다형성을 위해 사용, 추상메소드가 없어도 추상 클래스 가능

	abstract void draw(); // 추상 메소드, 선언은 했지만 구현은 없는 메소드, 상속받으면 무조건 구현 해줘야 함

	void tmp() {
	}; // 그냥 비워 둔 함수는 구현 안해도 상관 없음
}

class MyShape {
	MyShape() {
		x = 0;
		y = 0;
		color = "white";
	}

	MyShape(double _x, double _y, String _s) {
		x = _x;
		y = _y;
		color = _s;
	}

	double x, y;
	String color;

	void draw() {
		System.out.println("[SHAPE] (" + x + "," + y + ") 색 : " + color);
	}

}

class MyRect extends MyShape {
	MyRect(double _x, double _y, double _w, double _h, String _c) {
		super(_x, _y, _c); // 부모의 생성자를 이용해 저장
		w = _w;
		h = _h;

	}

	double w, h;

	@Override // 의도가 오버라이딩이라면
	void draw() {
		System.out.println("[RECT] (" + x + "," + y + ") (" + w + "," + h + ") 색 : " + color);
	}

	public boolean equals(Object obj) {
		if (obj instanceof MyRect) {
			MyRect r = (MyRect) obj;
			if (w == r.w && h == r.h)
				return true;
		}

		return false;
	}

	public String toString() {
		return "MyRect!!!!!";
	}
}

class MyCircle extends MyShape {
	MyCircle(double _x, double _y, double _r, String _c) {
		super(_x, _y, _c);
		r = _r;
	}

	double r;

	@Override
	void draw() {
		System.out.println("[CIRCLE] (" + x + "," + y + ") (" + r + ") 색 : " + color);
	}
}

public class Polymorphism {

	public static void draw(drawable o) { // 칼라그리기 기능이 있는 모든 객체를 인자로 받음
		o.colorDraw();
	}

	public static void main(String[] args) {

//		MyShape p = new MyShape(10, 10, "red");
//		MyRect q = new MyRect(20, 30, 40, 50, "blue");
//		MyCircle r = new MyCircle(40, 50, 10, "green");
//
//		p.draw();
//		q.draw();
//		r.draw(); 
//		여러개의 객체의 순서를 하나로 관리 하기위해선 super클래스의 배열(연결리스트)로 관리해야함

		MyShape[] arr = new MyShape[3];
		arr[0] = new MyShape(10, 10, "red");
		arr[1] = new MyRect(20, 30, 40, 50, "blue");
		arr[2] = new MyCircle(40, 50, 10, "green");

		for (int i = 0; i < arr.length; i++)
			arr[i].draw(); // MyShape 배열이지만 동적바인딩 되었기에 실제 대상의 오버라이딩된 함수들을 호출함
		// 하나의 draw()란 함수가 다르게 동작함 -> polymorphism

		for (int i = 0; i < arr.length; i++)
			System.out.println(arr[i]); // 모든 클래스는 Object클래스를 상속 받기에 toString()을 오버라이딩해 사용 가능

	}

}
