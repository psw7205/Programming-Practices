
public class MyFirstArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		double pi = 0.0;
		final int ITER_MAX = 10000; // 상수

		double sign = 1.0;

		for (int i = 0; i < ITER_MAX; i++) {
			double inc = 4.0 / (2 * i + 1);
			pi += (sign * inc);
			sign *= (-1.0);
			System.out.println("iter " + i + " : " + pi);
		}

		// int arr[10]; c 정적 할당
		// int* arr = (int*)malloc(sizeof(int)*10); c 동적할당
		// int* arr = new int [10]; c++ 동적할당

		int size = 10;
		int[] arr = new int[10];
		int arr2[] = new int[size]; // 자바에선 둘다 사용 가능
		int brr[] = arr; // 같은 공간을 가르킴

		for (int i = 0; i < arr.length; i++) { // 배열의 맴버변수로 길이를 가지고 있음
			arr[i] = 2 * i;
		}

		for (int i = 0; i < size; i++) {
			System.out.println(arr[i]);
		}

		arr2 = new int[5]; // 새롭게도 할당 가능

		for (int i = 0; i < size; i++) {
			System.out.println(brr[i]);
		}

		// 메모리 해제인 free나 delete 필요 없음 알아서 가비지컬렉션이 해제해 준다. garbage collection

		for (int elem : arr) // arr에 들어있는 모든 각각의 원소를 elem에 저장해서 순서대로 실행
		{ // foreach는 읽기 전용 수정 불가
			System.out.println(elem);
		}

		String names[] = { "사과", "배", "포도", "딸기" };
		for (String elem : names) {
			System.out.println(elem); // 스트링, enum등 모든 타입에 대해 사용 가능
		}

		int arr2d[][] = new int[2][5]; // 5개씩 2묶음 {{ 1,2,3,4,5 } , {1,2,3,4,5} }
		int brr2d[][] = new int[4][]; // 4묶음을 만드는데 각 묶음은 따로 만듬
		brr2d[0] = new int[10]; // 0번째 묶음은 10개
		brr2d[1] = new int[30]; // 1번째 묶음은 30개

	}

}
