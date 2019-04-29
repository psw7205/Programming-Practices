// 접근 지정자 : public - 누구나, protected - 상속끼리, private - 나만, 공백 - 같은 패키지끼리
// 퍼블릭 클래스는 하나의 자바파일에 1개만 존재하며 파일이름과 같아야함

class Student {
	public String name; // fields
	private int number;

	Student() {// 기본생성자는 다른 생성자가 있으면 따로 만들어줘야함, 다른 생성자가 없다면 자동으로 생성해줌
		name = "미정";
	}

	Student(String _name, int _num) {
		name = _name;
		number = _num;
	} // 생성자가 있으면 이 인수들이 꼭 필요함

	Student(int _num) {
		name = "미정";
		number = _num;
	} // overloading 같은 이름의 함수를 중복해서 사용가능 - 인자는 무조건 달라야함

	void print() { // methods
		System.out.println("이름: " + name + ", 학번 : " + number);
	}
}

public class MyFirstClass {

	public static void main(String[] args) {

		//Student a = new Student(); // 생성자가 충족되지 않기 떄문에 생성불가능
		Student a = new Student("박상우", 1); // 참조타입인 클래스는 new로 만들어서 가르키게 해야 사용가능
		Student b = a; // b가 a를 가르키기에 b를 바꾸면 a도 바뀜
		Student c = new Student("이영희", 1);
		
		a.name = "박상우";
		//a.number = 1;
		
		b.name = "김철수";
		//b.number = 2;
		
		//System.out.println("이름: " + a.name + ", 학번 : " + a.number);
		//System.out.println("이름: " + b.name + ", 학번 : " + b.number);
		//private인 number때문에 사용 불가능
		a.print();
		b.print();
		c.print();
		
	}

}
