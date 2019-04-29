
class Node { // 링크드 리스트 예시, 템플릿으로 구현 시 모든 자료형으로 사용 가능
	int value;
	Node next;

	void addTail(int v) {
		if (next == null) {
			Node n = new Node();
			n.next = null;
			n.value = v;
			this.next = n;
		} else {
			next.addTail(v);
		}
	}
}

class Box {
	int value;

	private Object value2;

	public Object getValue() {
		return value2;
	}

	public void setValue(Object in) {
		value2 = in;
	}

}

class Box2<T> { // 템플릿 클래스
	int value;

	private T value2;

	public T getValue() {
		return value2;
	}

	public void setValue(T in) {
		value2 = in;
	}
}

public class GeneralPractices {
	public static void func1(int x) {
		x = 20;
	}

	public static void func2(Box x) {
		x.value = 20;
	}

	public static String func3(String x) {
		x = "software";
		return x;
	}

	public static void main(String[] args) {
		int a = 10; // 변수 그 자체가 메모리
		func1(a); // 기본형은 함수에서 동작하는 방식이 달라짐
		System.out.println(a);

		Box b = new Box(); // b는 포인터, new로 메모리를 할당하고 b로 가르킴
		b.value = 10;
		func2(b); // 항상 콜 바이 레퍼런스
		System.out.println(b.value);

		// Integer c = new Integer("123");
		Integer c = Integer.valueOf("123"); // 위 두개는 같은 방법
		System.out.println(c);

		a = c; // unboxing wrapper -> 기본타입
		c = a; // boxing 기본타입 -> wrapper

		float d = c.floatValue();
		System.out.println(d);

		String str = "sejog univ.";
		str = func3(str); // string을 바꾸기 위해선 리턴값으로 x가 가르키는 위치를 반환해줘야 함
		System.out.println(str);

		Box e = new Box();
		e.setValue("park"); // Object로 받으면 모든 걸 다 저장할 수 있지만
		String str2 = (String) e.getValue(); // 꺼낼 때 개발자가 직접 정해줘야함 -> 실수가능성 많음
		System.out.println(str2);

		Box2<String> f = new Box2<String>(); // 이때 <T>를 String으로 바꿔 실제 클래스가 만들어짐
		f.setValue("kim");

		Box2<Integer> g = new Box2<>(); // 클래스만 가능, int 불가능
		g.setValue(123);

		Node n = new Node();

		n.value = 10;
		n.next = null;

		n.addTail(20);
		n.addTail(30);
		n.addTail(40);

		Node it = n;
		while (it != null) {
			System.out.println(it.value);
			it = it.next;
		}
	}
}
