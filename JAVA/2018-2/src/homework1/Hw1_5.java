package homework1;

import java.util.Scanner;

class MyConcertMenu { // 메뉴를 관리하는 클래스입니다.

	MySeat seat[] = new MySeat[3]; // 3종류의 좌석이 있습니다.
	Scanner in = new Scanner(System.in);

	MyConcertMenu() {
		for (int i = 0; i < seat.length; i++) {
			seat[i] = new MySeat(); // 생성자를 이용해 전부 초기화합니다.
		}
	}

	boolean Reserve() { // 예약메뉴입니다.
		System.out.print("좌석 구분 S(1), A(2), B(3)>>");
		int classNum = in.nextInt(); // 어떤 종류의 좌석인지 입력받습니다.
		switch (classNum) {
		case 1:
			System.out.print("S>>");
			break;
		case 2:
			System.out.print("A>>");
			break;
		case 3:
			System.out.print("B>>");
			break;
		default:
			System.out.println("잘못된 좌석입니다."); // 잘못된 번호가 들어오면 
			return false; //오류를 출력하고 false를 리턴합니다.
		}

		seat[classNum - 1].PrintMySeat(); // 현재 좌석의 상태를 나타냅니다.

		boolean tmp = false;

		System.out.print("이름>>");
		String name = in.next(); // 이름을 입력받고

		while (tmp == false) { // 제대로 설정될 때(SetMySeat 함수에서 true리턴)까지 계속 입력받습니다.
			System.out.print("번호>>"); // 번호를 입력받습니다.
			int num = in.nextInt(); 
			tmp = seat[classNum - 1].SetMySeat(name, num - 1);
		}
		return true;
	}

	void CheckMySeat() { // 조회메뉴입니다.
		System.out.print("S>>"); // 각 종류의 좌석을 전부 출력합니다.
		seat[0].PrintMySeat(); 
		System.out.print("A>>");
		seat[1].PrintMySeat();
		System.out.print("B>>");
		seat[2].PrintMySeat();
		System.out.println("<<<조회를 완료했습니다>>>");
	}

	boolean CancleMySeat() { // 취소메뉴입니다.
		System.out.print("좌석 구분 S(1), A(2), B(3)>>");

		int classNum = in.nextInt(); // 예약메뉴와 거의 동일합니다.

		switch (classNum) {
		case 1:
			System.out.print("S>>");
			break;
		case 2:
			System.out.print("A>>");
			break;
		case 3:
			System.out.print("B>>");
			break;
		default:
			System.out.println("잘못된 좌석입니다.");
			return false;
		}

		seat[classNum - 1].PrintMySeat();

		boolean tmp = false;

		while (tmp == false) { // 이름을 입력받는데 
			System.out.print("이름>>");
			String name = in.next();
			tmp = seat[classNum - 1].DeleteMySeat(name); // 이름이 제대로 지워지거나

			if (seat[classNum - 1].isEmpty() == true) { // 좌석이 모두 비어있으면 종료합니다.
				break;
			}
		}
		return true;
	}
}

class MySeat { // 좌석을 관리하는 클래스입니다.

	String seat[] = new String[10]; // 총 10개의 좌석입니다. 

	MySeat() {
		for (int i = 0; i < seat.length; i++) {
			seat[i] = " --- "; // 생성자를 이용해 " --- "로 초기화합니다.
		}
	}

	boolean isEmpty() { // 좌석이 비어있는지 검사하는 메소드입니다.
		int i = 0;

		for (i = 0; i < seat.length; i++) {
			if (seat[i] != " --- ") {
				break;
			}
		} // " --- "가 아니라면 이름이 입력되어있는 경우입니다.

		if (i == seat.length) { // i가 길이만큼 증가한 경우는 
			return true; // 끝까지 전부 " --- "이므로 이 좌석은 비어있는 경우입니다.
		} else {
			return false;
		}
	}

	boolean SetMySeat(String _name, int _num) { // 좌석 번호와 이름을 인자로 좌석을 설정하는 메소드입니다.
		if (_num < 0 || _num >= 10) { // 1~10이 아닌 번호가 들어왔을 때나
			System.out.println("잘못된 좌석번호입니다.");
			return false;
		}

		if (seat[_num] != " --- ") { // " --- "이 아니면 이미 예약된 좌석입니다.
			System.out.println("이미 예약된 좌석입니다.");
			return false;
		}
		// 위 두 경우가 아니라면 이름을 저장하고 true를 리턴합니다.
		seat[_num] = _name;
		return true;
	}

	void PrintMySeat() { // foreach문을 이용해 모든 값을 출력합니다.
		for (String s : seat) {
			System.out.print(s);
		}

		System.out.println();
	}

	boolean DeleteMySeat(String _name) { // 좌석에서 해당 이름을 지우는 메소드입니다.
		for (int i = 0; i < seat.length; i++) {
			if (seat[i].equals(_name) == true) { // 이름을 발견하면 
				seat[i] = " --- "; // " --- "로 초기화하고 true를 리턴합니다.
				return true;
			}
		}
		// 위에서 반환되지 않는다면 이름이 없는 것입니다.
		System.out.println("이름이 없습니다."); // false를 리턴합니다. 
		return false;
	}
}

public class Hw1_5 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("명품콘서트홀 예약 시스템입니다.");

		MyConcertMenu menu = new MyConcertMenu(); // 메뉴를 생성합니다. 

		while (true) {
			System.out.print("예약1, 조회:2, 취소:3, 끝내기:4>>");

			int num = in.nextInt();

			if (num == 4) { // 4가 입력되면 무한반복을 탈출하고 종료합니다.
				break;
			}

			boolean tmp = true;

			switch (num) {
			case 1:
				tmp = menu.Reserve(); // 1이 입력되면 예약을 실행하고

				while (tmp == false) { // 제대로 예약 될 때까지 입력받습니다.
					tmp = menu.Reserve();
				}
				break;
			case 2:
				menu.CheckMySeat(); // 조회를 실행합니다.
				break;
			case 3:
				tmp = menu.CancleMySeat(); // 예약과 마찬가지로 취소도 

				while (tmp == false) { // 제대로 취소 될 때까지 입력받습니다.
					tmp = menu.CancleMySeat();
				}
				break;
			default: // 1, 2, 3이 아니면 잘못된 입력입니다.
				System.out.println("잘못된 입력입니다.");
				break;
			}
		}

		in.close();
	}
}