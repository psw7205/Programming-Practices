class MyMath {
	static float pow(float in, int p) {
		float out = 1;
		for (int i = 0; i < p; i++)
			out *= in;
		return out;
	}
	// 자바에선 전역함수가 없기 떄문에 클래스 속에 있어야함
	// 스태틱으로 선언해야 클래스 명.함수() 접근 가능함
	// 객체를 만들 이유가 없는 클래스에서 사용 (math 클래스)
}

class Circle {
	public double radius = 12; // 자바는 이런 방식의 초기화도 지원함
	String name;
	static int repeat = 1; // static 변수는 new로 실제 객체를 만들기 전에 이미 만들어짐. 1개만 만들어지고 모든 객체에서 공유됨
	// 전역변수와 비슷

	Circle() {
		name = "untitled";
	}

	Circle(int _r, String _n) {
		radius = _r;
		name = _n;
	} // 같은 이름의 함수를 여러개 만드는 것 = 오버로딩
		// 인자를 보고 알아서 골라 실행됨

	void copyForm(Circle in) {
		radius = in.radius;
		name = new String(in.name); // 클래스의 복사는 이렇게 새로 할당하고 복사해야함
	}

	void print() {
		System.out.println("Circle: " + name + ", r = " + radius);
	}

	static void printRepeat() {
		System.out.println("repeat" + repeat);

	} // 스태틱 함수는 스태틱 함수만 호출 가능
}

public class MySecondClass {

	public static void main(String[] args) {
		Circle a = new Circle();
		Circle b = new Circle(100, "빈대떡");
		// b = a; // b가 a를 가르키게 바뀌기 때문에 a가 바뀌면 b도 바뀜. 복사가 아님

		Circle.repeat = 2; // static변수는 클래스 이름을 통해서도 접근 가능
		//Circle.repeat();

		a.name = "피자";

		a.print();
		b.print();

		// String str = "세종대학교";
		// String str = new String("세종대학교"); 위 두개는 같다.

		b.copyForm(a); // 복사 함수를 만들어 사용
		b.print();

		Circle[] c = new Circle[10]; // 레퍼런스 배열

		// c[0].radius = 10; // 레퍼런스 변수를 초기화 한적 없는데 값을 줄 수 없음. 널포인트익셉션 예외 발생

		for (int i = 0; i < 10; i++)
			c[i] = new Circle(); // 각각 초기화를 해줘야 사용 가능

		c[0].radius = 10;

	}

}
