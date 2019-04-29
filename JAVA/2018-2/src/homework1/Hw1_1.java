package homework1;

import java.util.Scanner;

public class Hw1_1 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("첫번째 원의 중심과 반지름 입력>>");

		double x = in.nextDouble();
		double y = in.nextDouble();
		double r = in.nextDouble();

		System.out.print("두번째 원의 중심과 반지름 입력>>");

		double x1 = in.nextDouble();
		double y1 = in.nextDouble();
		double r1 = in.nextDouble();

		double tmp = Math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1));

		if (tmp < r + r1) {
			System.out.println("두 원은 겹칩니다.");
		} else {
			System.out.println("두 원은 겹치지 않습니다.");
		}

		in.close();

	}

}
