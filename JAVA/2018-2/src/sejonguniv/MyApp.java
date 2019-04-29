package sejonguniv;

// import sejonguniv.software.MyMath;
import sejonguniv.software.*; // 이 패키지 아래에 있는 모든 클래스 사용 가능
// import : 찾다가 모르는 함수가 나오면 이 패키지 속 함수인지 확인해봐라
// 보통 소문자로 작성, 큰개념 -> 작은개념
// 디렉토리상 아래에 있더라도 소속관계는 없다, 서로 독립적임

class MyPoint { // extends java.lang.Object가 자동적으로 상속됨
	double x, y;

	MyPoint(double _x, double _y) {
		x = _x;
		y = _y;
	}

	@Override // equals 재정의 해야 사용 가능
	public boolean equals(Object obj) {
		if (!(obj instanceof MyPoint))
			return false;

		MyPoint in = (MyPoint) obj;

		if (this.x == in.x && this.y == in.y)
			return true;

		return false;

	}

	@Override
	public String toString() {
		// 내가 어떤 클래스인지 알려주는 getClass()에 이름을 알려주는 toString()
		return this.getClass().toString() + "(" + x + " , " + y + ")";
	}
}

public class MyApp {

	public static void main(String[] args) {
		int x = 10;
		int y = 20;
		// int z = sejonguniv.software.MyMath.add(x,y); // 다른 패키지라면 항상 풀네임으로 호출해야함
		int z = MyMath.add(x, y); // 임포트를 통해 줄여 쓸 수 있음
		int w = MyCalc.mul(x, y); // 같은 패키지라면 그냥 사용 가능

		System.out.println(z);
		System.out.println(w);

		MyPoint p = new MyPoint(1, 2);
		MyPoint p2 = new MyPoint(1, 2);

		if (p == p2) // 레퍼런스 "주소"가 같은지 다른지 비교
			System.out.println("equal");
		else
			System.out.println("Not equal");

		if (p.equals(p2)) // 내용을 비교
			System.out.println("equal");
		else
			System.out.println("Not equal");

		System.out.println(p); // print는 클래스 객체가 인자로 넘어오면 자동으로 toString()호출
		System.out.println(p.hashCode()); // 데이터를 정수로 바꿔주는 메소드
	}

}