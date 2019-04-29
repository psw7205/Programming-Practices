class Point2D {
	double x, y;

	static double getDistance(Point2D a, Point2D b) {
		return Math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));

	} // 2점의 거리를 구하는 함수

	double getDistanceFromMe(Point2D in) {
		return getDistance(this, in); // 나와 in사이의 거리를 return, 함수를 재사용
	} // 나와 점 사이의 거리
} // this레퍼런스 사용 예제

//regNum should be unique
// if regNum is not ready, you can not make a client

class Client {
	static int numClient = 0;
	final static int OFFSET = 100;

	String name; // 이름
	String tel; // 전화번호
	int regNum; // 고객번호, 중복되면 안됨, 번호가 만들어져야 생성가능

	private Client() {
		numClient++;
		regNum = numClient + OFFSET;
	} // 이름이나 번호가 있어야만 생성가능해야하므로 private로 

	Client(String _name) {
		this();
		name = _name;
	}

	Client(String _name, String _tel) {
		this(_name); // 생성자에서 다른 생성자를 호출할 때 사용
		tel = _tel;
	} // 코드 관리 용이

	void print() {
		System.out.println("고객번호 " + regNum + " 이름 " + name);

		if (isLastClient(this)) { // this의 사용법
			System.out.println("-------------------------------------------------------");
		}
	}

	static boolean isLastClient(Client in) {
		if (numClient + OFFSET == in.regNum)
			return true;
		return false;
	}
}

public class ClassPractice {

	public static void main(String[] args) {

		Client[] client = new Client[3];

		client[0] = new Client("david");
		client[1] = new Client("albus");
		client[2] = new Client("boris");

		for (int i = 0; i < 3; i++) {
			client[i].print();
		}

		Client.isLastClient(client[2]);
	}

}
