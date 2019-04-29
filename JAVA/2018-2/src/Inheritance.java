
class ColorPoint extends Point { // point 클래스를 확장 시켜 ColorPoint 클래스를 만듦 (상속)
	String color;

	ColorPoint() // 기본으로 부모의 디폴트 생성자를 호출함
	{
		// super(); 가 기본으로 숨어있어 언제나 제일 먼저 실행됨
		color = "white";
	}

	ColorPoint(double _x, double _y) {
		// this(); 와 super(); 는 맨 윗줄에 있어야 하므로 동시에 사용 못함
		super(_x, _y); // 부모클래스의 생성자를 호출 할 때 super()를 사용
		color = "white";
	}

	ColorPoint(double _x, double _y, String _color) {
		super(_x, _y);
		color = _color;
	}

	void ColorPrint() {
		print(); // 컬러포인터에는 구현되어있지 않지만 포인터 클래스에 구현되어있는 함수 사용 가능
		System.out.println("color -> " + color);
	}

	@Override // 이 단어가 나오면 컴파일러가 바로 밑 함수가 부모에 존재하는 함수가 있는지 알려줌 -> 오탈자 발견 가능
	void print() // 함수이름을 같게 만들어 자식 함수가 부모 함수를 바꿔치기함 -> 오버라이딩
	{
		super.print(); // 부모의 함수를 호출할 땐 super를 사용해 명시적으로 표시함
		System.out.println("color -> " + color);
	}
}

class Point {
	final static double MAX_X = 100;
	final static double MAX_Y = 100;
	private double x, y; // 데이터는 전부 프라이빗으로 막아두고

	Point() {
		setX(0);
		setY(0);
	}

	Point(double _x, double _y) {
		setX(_x);
		setY(_y);
	}

	// setter : mutator
	public void setX(double in) {
		x = (in < MAX_X) ? in : MAX_X;
	} // 함수를 이용해 사용자가 바꿀 수 있는 값을 지정해 줌

	public void setY(double in) {
		y = (in < MAX_Y) ? in : MAX_Y;
		;
	}

	// getter : accessor
	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	void print() {
		System.out.println(x + "," + y);
	}

	static double getDistance(Point a, Point b) {
		return Math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
	}
}

public class Inheritance {

	public static void main(String[] args) {

		Point a = new Point(50, 50);
		a.print();

		ColorPoint b = new ColorPoint();
		b.ColorPrint();
		b.print();
	
	
		System.out.println(Point.getDistance(a, b)); // b는 칼라포인트지만 부모클래스로 포인터를 가지고 있기에 바로 사용 가능
		
		Point c = b; // 자식클래스 중에 부모클래스 부분만 사용, 부모의 레퍼런스는 언제나 자식을 가르킬 수 있음 sub->super : upcasting
	
		c.setX(10);
		c.print(); // 포인트 클래스이지만 실제로 가르키는 내용은 칼라포인트 클래스이기에 칼라포인트의 print()가 호출됨
		// dynamic binding, polymorphism 이름은 같은데 가르키는 내용에 따라 다르게 동작함
		
		//ColorPoint d = a; // 자식이 부모를 가르킴 down casting,할 수 없는 일을 시킬 수 있기 때문에 금지 // 
		ColorPoint d = (ColorPoint) c; // d->c->b 결국 b(colorPoint)를 가르키기에 강제 형변환 사용 가능
	}

}
