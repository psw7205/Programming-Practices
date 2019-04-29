package homework1;

import java.util.Scanner;

public class Hw1_2 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("연산>>");

		double a = in.nextDouble();
		String op = in.next();
		double b = in.nextDouble();

		if (b == 0) { // 0으로 나누는 경우
			System.out.println("0으로 나눌 수 없습니다.");
		} else { // 아닐경우
			System.out.print(a + op + b + "의 계산 결과는 ");

			if (op.equals("+") == true) {
				System.out.println(a + b);
			} else if (op.equals("-") == true) {
				System.out.println(a - b);
			} else if (op.equals("*") == true) {
				System.out.println(a * b);
			} else { // 연산자가 총 4종류만 들어오기에 나누기는 else를 사용했습니다.
				System.out.println(a / b);
			}
		}
		in.close();
	}
}