import java.util.Scanner;

class MyArrayIdxNegativeException extends Exception {
// Exception을 상속받아 새로운 예외처리 클래스를 만들 수 있음
}

class MyArrayIdxtoBigException extends Exception {

}

public class ExceptionPractice {

	// c에서 사용하던 예외처리 방법
	public static boolean setInput(int arr[], int idx, int value) {
		if (idx < 0 || idx > arr.length - 1)
			return false;

		arr[idx] = value;
		return true;
	}

	public static void setInput2(int arr[], int idx, int value)
			throws MyArrayIdxNegativeException, MyArrayIdxtoBigException {
		// throws가 있으면 무조건 예외처리를 해줘야함, 여러개 thorw 할 수 있음
		if (idx < 0) {
			MyArrayIdxNegativeException e = new MyArrayIdxNegativeException();
			throw e;
		}

		if (idx > arr.length - 1) {
			MyArrayIdxtoBigException e = new MyArrayIdxtoBigException();
			throw e;
		}

		arr[idx] = value;
	}

	public static void main(String[] args) {

		/*
		 * int x = 10; int y = 0; int z = 0;
		 * 
		 * try { z = x / y; // 0으로 나누기 } catch (ArithmeticException e) { z = 0; }
		 * 
		 * int arr[] = new int[10];
		 * 
		 * try { arr[10] = 100; // 배열 인덱스 범위 밖에 접근 } catch
		 * (ArrayIndexOutOfBoundsException e) { System.out.println("Wrong Array index");
		 * }
		 * 
		 * Scanner input = null; // null 포인터를 사용함 input.nextInt();
		 */

		int arr[] = new int[10];

		if (!setInput(arr, 10, 100))
			System.out.println("error");
		// c에서 사용하던 에러 체크 방법, 단점 : 어떤 문제가 생겼는지 모름, 리턴이 bool타입이기에 다른 리턴값을 못 가져옴

		int arr2[] = new int[10];

		try {
			setInput2(arr2, 1, 100);
			int x = 10;
			int y = 0;
			int z = x / y;
		} catch (MyArrayIdxNegativeException e) {
			System.out.println("Negative index error !");
		} catch (MyArrayIdxtoBigException e) {
			System.out.println("Too Big index error !");
		} catch (ArithmeticException e) {
			System.out.println("Do not divide by zero !");
		} catch (Exception e) {
			System.out.println("나머지 에러 다 받음");
			// 얘가 맨 위에 있으면 얘가 에러를 다 받기에 나머지 에러들은 처리가 안됨
		}

	}

}