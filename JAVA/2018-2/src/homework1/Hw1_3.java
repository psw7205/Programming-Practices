package homework1;

import java.util.Scanner;

public class Hw1_3 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("정수 몇개>>");

		int n = in.nextInt();

		int ar[] = new int[n];

		for (int i = 0; i < n; i++) {
			ar[i] = (int) (Math.random() * 100 + 1); // 1~100까지 랜덤 값을 저장합니다.
			for (int j = 0; j < i; j++) { // 이중반복문을 이용해 앞에서 현재 위치까지 확인하는데
				if (ar[j] == ar[i]) { // 중복된 값이 앞에서 나온 경우
					i--; // i를 1 줄여 다시 그 위치에 랜덤 값을 저장합니다.
					break;
				}
			}
		}

		int cnt = 0;

		for (int x : ar) {
			if (cnt % 10 == 9) { // 책의 예시처럼 표시하기 위해 10칸씩 나눠 표시했습니다.
				System.out.println(" " + x);
			} else {
				System.out.print(" " + x);
			}
			cnt++;
		}

		in.close();
	}
}