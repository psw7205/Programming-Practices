package homework2;

import java.util.Scanner;

abstract class Shape {
	private Shape next;

	public Shape() {
		next = null;
	}

	public void setNext(Shape obj) {
		next = obj;
	}

	public Shape getNext() {
		return next;
	}

	public abstract void draw();
}

class Line extends Shape {

	@Override
	public void draw() {
		System.out.println("Line");
	}

}

class Rect extends Shape {

	@Override
	public void draw() {
		System.out.println("Rect");
	}

}

class Circle extends Shape {

	@Override
	public void draw() {
		System.out.println("Circle");
	}

}

class GraphicEditor {
	String name;
	Shape list;
	int cnt;

	GraphicEditor(String in) {
		name = in;
		cnt = 0;
	}

	void add(int in) {
		cnt++;
		Shape tmp = null;
		switch (in) {
		case 1:
			tmp = new Line();
			break;
		case 2:
			tmp = new Rect();
			break;
		case 3:
			tmp = new Circle();
			break;
		default:
			break;
		}

		Shape head = list;

		if (head == null) {
			list = tmp;
			return;
		}

		while (head.getNext() != null) {
			head = head.getNext();
		}
		head.setNext(tmp);
		return;
	}

	boolean delete(int in) {

		if (in >= cnt)
			return false;

		Shape head = list;
		
		if (in == 0) {
			list = head.getNext();
			return true;
		}

		Shape tmp = head;
		for (int i = 0; i < in; i++) {
			tmp = head;
			head = head.getNext();
		}

		tmp.setNext(head.getNext());
		return true;
	}

	void print() {
		Shape tmp = list;
		while (tmp != null) {
			tmp.draw();
			tmp = tmp.getNext();
		}
	}

	void startProgram() {
		Scanner in = new Scanner(System.in);
		System.out.println("그래픽에디터 " + name + "을 실행합니다.");

		while (true) {
			System.out.print("삽입(1), 삭제(2), 모두보기(3), 종료(4)>>");
			int tmp = in.nextInt();
			int num = 0;

			if (tmp == 4)
				break;

			switch (tmp) {
			case 1:
				System.out.print("Line(1), Rect(2), Circle(3)>>");
				num = in.nextInt();
				this.add(num);
				break;
			case 2:
				System.out.print("삭제할 도형의 위치>>");
				num = in.nextInt();
				if (this.delete(num))
					System.out.println("삭제되었습니다.");
				else
					System.out.println("삭제할 수 없습니다.");
				;
				break;
			case 3:
				this.print();
				break;
			default:
				break;

			}
		}

		System.out.println(name + "을 종료합니다.");
		in.close();
		return;
	}

}

public class Hw2_2 {

	public static void main(String[] args) {
		GraphicEditor myEditor = new GraphicEditor("beauty");
		myEditor.startProgram();
	}

}
