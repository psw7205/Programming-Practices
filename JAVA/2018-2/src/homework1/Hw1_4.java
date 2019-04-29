package homework1;

public class Hw1_4 {

	public static void main(String[] args) {

		int ar[][] = new int[4][4]; // 4X4행렬입니다.

		for (int i = 0; i < 10; i++) {
			int x = (int) (Math.random() * 4); // 0~3까지 랜덤좌표입니다.
			int y = (int) (Math.random() * 4);

			while (ar[x][y] != 0) { // 해당 좌표의 값이 0이 아니면 이미 다른 값이 들어와 있는 경우입니다.
				x = (int) (Math.random() * 4); // 해당 좌표 값이 0이 될 때까지 랜덤으로 x, y를 설정합니다.
				y = (int) (Math.random() * 4);
			}

			ar[x][y] = (int) (Math.random() * 10 + 1); // 1~10까지 랜덤 값을 저장합니다.
		}

		for (int i = 0; i < ar.length; i++) {
			for (int j = 0; j < ar[i].length; j++)
				System.out.print(ar[i][j] + "\t");
			System.out.println();
		}
	}
}
